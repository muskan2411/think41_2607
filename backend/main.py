from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["conversational_ai"]
messages_col = db["messages"]
conversations_col = db["conversations"]
users_col = db["users"]

# Pydantic input model
class ChatInput(BaseModel):
    user_id: str
    message: str
    conversation_id: str | None = None  # New or existing conversation

@app.post("/api/chat")
def chat_endpoint(chat: ChatInput):
    # Step 1: Create conversation if not provided
    if not chat.conversation_id:
        convo = {
            "user_id": chat.user_id,
            "started_at": datetime.utcnow()
        }
        convo_id = conversations_col.insert_one(convo).inserted_id
    else:
        convo_id = chat.conversation_id

    # Step 2: Store user message
    user_msg = {
        "conversation_id": convo_id,
        "sender": "user",
        "message": chat.message,
        "timestamp": datetime.utcnow()
    }
    messages_col.insert_one(user_msg)

    # Step 3: (Dummy) AI response
    ai_reply = f"You said: {chat.message}"

    # Step 4: Store AI response
    ai_msg = {
        "conversation_id": convo_id,
        "sender": "ai",
        "message": ai_reply,
        "timestamp": datetime.utcnow()
    }
    messages_col.insert_one(ai_msg)

    return {
        "conversation_id": str(convo_id),
        "response": ai_reply
    }
