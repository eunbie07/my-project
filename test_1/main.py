from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://localhost"] 등
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    emotion: str
    spending: str

@app.post("/chat")
def chat(data: ChatRequest):
    prompt = (
        f"당신은 한국어만 사용하는 감정 소비 전문 심리 상담사입니다.\n\n"
        f"지금 나는 '{data.emotion}' 감정을 느끼고 있고, "
        f"'{data.spending}'에 돈을 썼어. 이 소비가 충동적인 건지, "
        f"그리고 나에게 감정적으로 도움이 되는 간단한 조언을 한 문장으로 해줘.\n\n"
        f"꼭 한국어로만 답변해줘."
        f"한자, 일본어, 중국어쓰지 말아줘"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "openhermes:latest",  # 여기만 수정
            "prompt": prompt,
            "stream": False
        }
    )
    result = response.json()["response"]
    return {"result": result}
