# Streamlit UI app
import streamlit as st
from chatbot import get_bot_response
from memory import save_conversation, load_conversation

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("AI Chatbot Powered by Ollama + LangChain")

# Load previous conversation if any
if "messages" not in st.session_state:
    st.session_state.messages = load_conversation()

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Take user input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({
        "role": "user",
        "content": user_input})

    # Get bot response
    response = get_bot_response(user_input)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append({
        "role": "assistant",
        "content": response})

    # Save updated conversation
    save_conversation(user_input, bot_response=response)

    # st.session_state.messages Keeps chat memory in the web app session
    # chat_input(...) Gets user input like a real
    # st.chat_message(...) Stream_lit’s way of showing styled chat
    # ave_conversation(...) Writes the chat to a file (JSON)



