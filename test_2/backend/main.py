from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정 (React → FastAPI 요청 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": f"""
사용자의 입력: "{req.message}"
이 사람이 감정적인 소비를 했는지 간단히 판단하고,
짧고 따뜻한 한 문장으로 공감과 조언을 해줘. 너무 길지 않게, 말투는 부드럽게. 한국어로만 말해.
""",
        "stream": False
    })
    data = response.json()
    return {"response": data["response"]}
