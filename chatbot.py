import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="ChatBot 101", layout="centered")

# Dark theme styling
st.markdown("""
<style>
    body {
        background-color: #121212;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    .message {
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
    }
    .user {
        background-color: #1f6f8b;
        color: white;
        text-align: right;
    }
    .bot {
        background-color: #99c24d;
        color: black;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🤖 ChatBot 101</h1>", unsafe_allow_html=True)

# Response function
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I assist you?"
    elif "how are you" in user_input:
        return "I'm great, thanks for asking! 😊"
    elif "your name" in user_input:
        return "I'm ChatBot 101 🤖, your virtual buddy!"
    elif "time" in user_input:
        return "⏰ It's " + datetime.now().strftime("%H:%M:%S")
    elif "bye" in user_input:
        return "Goodbye! See you soon! 👋"
    else:
        return "Sorry 😔, I didn’t get that."

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Chat input with instant processing
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat.append(("You", user_input + " 😊"))
    response = get_bot_response(user_input)
    st.session_state.chat.append(("Bot", response))

# Show conversation
for sender, message in st.session_state.chat:
    class_name = "user" if sender == "You" else "bot"
    st.markdown(f"<div class='message {class_name}'><strong>{sender}:</strong> {message}</div>", unsafe_allow_html=True)
