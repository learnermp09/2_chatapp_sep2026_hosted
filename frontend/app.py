import streamlit as st
import requests

BASE_URL = "https://two-chatapp-sep2026-hosted.onrender.com"
# API_URL = "http://127.0.0.1:8000"

st.title("✨Langserve-based LLM AI Chatbot")

st.info(
    """
    ℹ️ **Backend Wake-Up Notice**

    The AI backend is hosted on a cloud service that automatically sleeps during periods
    of inactivity. The first request may take **30–90 seconds** while the service wakes up.

    Once active, responses are typically generated within a few seconds.

    Thank you for your patience.
    """
)

# API endpoint
BASE_URL = "https://two-chatapp-sep2026-hosted.onrender.com"


# Groq assistant
st.image("https://cdn.sanity.io/images/chol0sk5/production/ce0b2266373b3c9722b0bccb9a98441c26c89696-1200x630.png", width=120)

GROQ_ENDPOINT = f"{BASE_URL}/chatgroq/invoke"

groq_question = st.text_input("Enter your question here")

if groq_question:
    response = requests.post(GROQ_ENDPOINT, json={"input": {"question":groq_question}})
    if response.status_code == 200:
        # with LangServe's /invoke endpoint, the response is generally wrapped as an output
        answer = response.json().get("output", "No output found")
    else:
        answer = f"{response.status_code} : {response.text}"
    st.write(answer)

# OpenAI assistant
st.image("https://assets.qz.com/media/whatisopenai-qz-1400x788.jpg", width = 120)

OPENAI_ENDPOINT = f"{BASE_URL}/chatopenai/invoke"

openai_question = st.text_input("Enter your question here")

if openai_question:
    response = requests.post(OPENAI_ENDPOINT, json = {"input" :{"question" : openai_question}})
    if response.status_code == 200:
        answer = response.json().get("output", "No output found")
    else:
        answer = f"{response.status_code} : {response.text}"
    st.write(answer)