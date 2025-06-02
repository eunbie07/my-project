
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_history = [
    {
        "role": "system",
        "content": (
            "너는 감정-소비 챗봇이야. 사용자가 소비 후 느끼는 감정을 공감하고, "
            "소비 이유를 함께 되짚어보며, 자연스럽게 스스로 반성하거나 대안을 생각하게 도와줘. "
            "답변은 따뜻하게, 2~3문장 이내로 대화하듯 해줘."
        )
    }
]

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    user_input = msg.message

    prompt = f'''
    사용자 입력: "{user_input}"

    역할:
    - 감정에 공감하고
    - 소비 이유를 질문하며 돌아보게 하고
    - 너무 길지 않게, 2~3문장 대화처럼 이어줘
    '''

    chat_history.append({"role": "user", "content": prompt})
    response = ollama.chat(model="gemma:2b", messages=chat_history)
    reply = response["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})

    return {"response": reply}
