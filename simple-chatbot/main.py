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

# 전체 대화 저장 (단일 사용자 기준)
chat_history = [
    {
        "role": "system",
        "content": (
            "너는 감정과 소비에 대해 짧고 따뜻하게 공감해주는 챗봇이야. "
            "사용자의 소비와 감정을 파악하고, 너무 길지 않은 위로 또는 조언을 해줘. "
            "대답은 한 문장 이내로 해줘."
        )
    }
]

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    user_input = msg.message

    # ✅ 여기에 너가 말한 프롬프트 넣기
    prompt = f"""
    너는 감정-소비 반성 챗봇이야.

    사용자 입력: "{user_input}"

    조건:
    - 사용자 감정에 짧게 공감해줘
    - 어떤 소비를 했는지 이해하고, 그 이유를 부드럽게 질문해줘
    - 너무 긴 말은 피하고, **2문장 이내로 실용적인 말**만 해줘
    - 철학적이거나 뜬구름 잡는 말은 하지 마
    - 자연스럽고 따뜻한 말투로 말해줘
    """

    chat_history.append({"role": "user", "content": prompt})
    response = ollama.chat(model="gemma:2b", messages=chat_history)
    reply = response["message"]["content"]
    chat_history.append({"role": "assistant", "content": reply})

    return {"response": reply}
