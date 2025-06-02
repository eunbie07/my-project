
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from emotion import analyze_emotion
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(msg: Message):
    user_input = msg.message
    emotion = analyze_emotion(user_input)

    prompt = f"""
    너는 감정-소비 상담 챗봇이야.
    사용자 입력: "{user_input}"
    감정 상태: {emotion}
    이 감정에 공감하고 과소비 방지에 도움이 되는 조언을 공감하며 해줘.
    """

    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
