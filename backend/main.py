from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
load_dotenv(BASE_DIR/".env")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LLM chatbot API is running"}
@app.get("/health")
def health():
    return {"status": "healthy"}

class Question(BaseModel):
    question: str = Field(
        ...,
        title = "User's Question",
        description = "Please enter your prompt here",
        examples = ["What is harness engineering?"]
    )

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Please answer the user's query."),
    ("user", "Question: {question}")
])

# LLM
llm = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0)

# String parser
parser = StrOutputParser()

chain = prompt | llm | parser

add_routes(app, chain.with_types(input_type = Question), path = "/chatgroq")


