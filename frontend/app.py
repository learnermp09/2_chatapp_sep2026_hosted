import streamlit as st
import requests

BASE_URL = "https://two-chatapp-sep2026-hosted.onrender.com"

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

# Groq assistant
st.image("https://cdn.sanity.io/images/chol0sk5/production/ce0b2266373b3c9722b0bccb9a98441c26c89696-1200x630.png", width=120)

GROQ_ENDPOINT = f"{BASE_URL}/chatgroq/invoke"

groq_question = st.text_input("Enter your question here", key="groq_input")

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

openai_question = st.text_input("Enter your question here", key="openai_input")

if openai_question:
    response = requests.post(OPENAI_ENDPOINT, json = {"input" :{"question" : openai_question}})
    if response.status_code == 200:
        answer = response.json().get("output", "No output found")
    else:
        answer = f"{response.status_code} : {response.text}"
    st.write(answer)

# GeminiAI assistant
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz8EMBITBMMyuc8k2xMj_05GN8b_XxgwaBgIFAqpOI1DwF4yQa6kvMfU2g&s=10", width = 120)

GEMINIAI_ENDPOINT = f"{BASE_URL}/chatgeminiai/invoke"

gemini_question = st.text_input("Enter your question here", key = "gemini_input")

if gemini_question:
    response = requests.post(GEMINIAI_ENDPOINT, json = {"input" : {"question": gemini_question}} )
    if response.status_code == 200:
        answer = response.json().get("output", "No output found")
    else:
        answer = f"{response.status_code} : {response.text}"
    st.write(answer)