# ChromaDB logic
# This file handles saving and loading past user-bot conversations so the chatbot
# can “remember” and learn from previous chats.

import json
from pathlib import Path

DATA_FILE = Path("data/conversations.json")

# save conversations to JSON


def save_conversation(user_input, bot_response):
    messages = load_conversation()
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": bot_response})
    with open(DATA_FILE, "w") as f:
        json.dump(messages, f, indent=4)

# load all past conversation


def load_conversation():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
