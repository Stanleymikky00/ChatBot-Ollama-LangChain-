## AI Chatbot Powered by Ollama + LangChainLangChain

This is a custom AI chatbot built using:
- [Ollama](https://ollama.com/) (for running local LLMs like LLaMA3)
- [LangChain](https://www.langchain.com/) (for managing LLM chains and memory)
- [Streamlit](https://streamlit.io/) (for the web-based chat UI)
- [ChromaDB](https://www.trychroma.com/) (optional, for future vector memory)

---

##  Features

-  Local LLM chatbot (no API cost!)
-  Memory: Stores previous conversations
-  Built-in JSON file for history
-  Web UI with Streamlit
-  Runs completely offline

---

##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/ai-chatbot.git
   cd ai-chatbot

#Create a virtual environment:
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

#Install dependencies:
pip install -r requirements.txt

#Run Ollama and pull the model:
ollama run llama3

#Start the app:
streamlit run app.py

#Project Structure
├── app.py              # Streamlit frontend
├── chatbot.py          # Handles response logic with LangChain + Ollama
├── memory.py           # Manages saving/loading chat history
├── config.py           # Model config
├── requirements.txt    # Python dependencies
├── conversations.json  # Chat memory
└── README.md           # You are here!

# Notes
Make sure Ollama is running in the background.
Chat history is saved in data/conversations.json.

#Author
Stanley Mike
