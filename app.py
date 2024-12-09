"""Gemini Chat Assistant Streamlit App"""

import os
import uuid

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse.callback import CallbackHandler

# Load environment variables
load_dotenv()

# Initialize Streamlit page configuration
st.set_page_config(page_title="Gemini Chat Assistant", page_icon="🤖", layout="centered")

# Custom CSS for better appearance
st.markdown(
    """
    <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stButton>button {
            border-radius: 10px;
            width: 100%;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            flex-direction: column;
        }
        .user-message {
            background-color: #e6f3ff;
        }
        .assistant-message {
            background-color: #f0f2f6;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# System prompt to restrict AI responses
SYSTEM_PROMPT = (
    "You are an AI assistant specialized in AI, ML, and LLMs. "
    "You should only respond to questions related to these topics, "
    "focusing on Gemini, Gemma, and BERT models."
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Welcome! I'm an AI assistant powered by Gemini models. How can I help you today?",
        }
    ]

if "langfuse_handler" not in st.session_state:
    st.session_state.langfuse_handler = CallbackHandler(
        public_key=os.environ["PUBLIC_KEY"],
        secret_key=os.environ["SECRET_KEY"],
        host=os.environ["HOST"],
        session_id=str(uuid.uuid4()),
        user_id=str(uuid.uuid4()),
    )

if "llm" not in st.session_state:
    st.session_state.llm = ChatGoogleGenerativeAI(
        model="gemini-exp-1206",
        temperature=0,
        max_tokens=512,
        timeout=None,
        max_retries=2,
    )

# Display header
st.title("💬 Gemini Chat Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        try:
            response = st.session_state.llm.stream(
                SYSTEM_PROMPT + "\n\n" + prompt,
                config={"callbacks": [st.session_state.langfuse_handler]},
            )

            # Use st.write_stream to display the response
            st.write_stream(response)

            # Add AI response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": str(response)}
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Add a clear chat button in the main area
if st.button("Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Welcome! I'm an AI assistant powered by Gemini models. How can I help you today?",
        }
    ]
    st.rerun()
