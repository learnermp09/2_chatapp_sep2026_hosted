import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("✨Langserve-based LLM AI Chatbot")

input_text = st.text_input("Enter your question here")

if input_text:
    response = requests.post(f"{API_URL}/chatgroq/invoke", json={"input": {"question": input_text}})
    if response.status_code == 200:
        # with LangServe's /invoke endpoint, the response is generally wrapped as an output
        answer = response.json().get("output", "No output found")
    else:
        answer = f"{response.status_code} : {response.text}"
    st.write(answer)
