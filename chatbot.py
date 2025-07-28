# Core AI logic (Ollama connection)
# Use LangChain to build a prompt.
# Connect with the Ollama LLM (e.g. llama3).
# Fetch responses based on current + past conversations.
# THIS WHOLE PROJECT IS BUILT ON “RAG” (Retrieval-Augmented Generation) — not
# retraining, but augmenting the model with external memory.

from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


# Initialize Ollama model (make sure it's running: `ollama run llama3`)
llm = Ollama(model="llama3")

# Use memory to store conversation context within session
memory = ConversationBufferMemory()


# LangChain conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,  # shows what's going on the inside
)


def get_bot_response(user_input):
    return conversation.predict(input=user_input)


# Ollama(model="llama3"): Connects to your local LLM.
# ConversationBufferMemory(): Keeps chat history in memory (RAM).
# ConversationChain: A LangChain tool to handle multi-turn chats.
# get_bot_response(user_input): Takes user input, returns bot reply.
