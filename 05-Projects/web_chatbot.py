"""
Streamlit Web Chatbot
=====================

A simple, modern web interface for your chatbot using Streamlit.
This script demonstrates how to take your CLI chatbot and give it a GUI!

Usage:
    streamlit run 05-Projects/web_chatbot.py

Author: Zero-To-GenAI Course
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# ===========================================
# SETUP
# ===========================================

# Load API key
load_dotenv()

# Page Config
st.set_page_config(page_title="Zero-To-GenAI Chatbot", page_icon="🤖")

# Title
st.title("🤖 AI Assistant")
st.caption("Built with OpenAI + Streamlit")

# Initialize OpenAI Client
if "OPENAI_API_KEY" not in os.environ:
    st.error("❌ OPENAI_API_KEY not found. Please check your .env file.")
    st.stop()

client = OpenAI()

# ===========================================
# SESSION STATE (MEMORY)
# ===========================================

# Streamlit reruns the script on every interaction.
# We use st.session_state to persist data (like chat history) between reruns.

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# ===========================================
# UI: DISPLAY CHAT HISTORY
# ===========================================

# Display all messages except the system message
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ===========================================
# UI: USER INPUT & AI RESPONSE
# ===========================================

if prompt := st.chat_input("What is on your mind?"):
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Add to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response (looks cool!)
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            stream=True,
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # 4. Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
