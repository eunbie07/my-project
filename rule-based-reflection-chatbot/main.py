
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

# 간단한 감정 키워드 사전
emotion_keywords = {
    "우울": ["우울", "슬퍼", "속상", "눈물"],
    "불안": ["불안", "초조", "걱정"],
    "짜증": ["짜증", "화나", "열받"],
    "기쁨": ["기뻐", "좋아", "행복"]
}

# 반응 규칙
def analyze_message(text):
    emotion_detected = "중립"
    for emotion, keywords in emotion_keywords.items():
        if any(kw in text for kw in keywords):
            emotion_detected = emotion
            break

    if emotion_detected == "우울":
        return "마음이 무거운 날이셨군요. 그 소비가 위로가 되었나요?"
    elif emotion_detected == "불안":
        return "불안한 기분일 땐 지출이 늘기도 하죠. 어떤 생각으로 소비하신 걸까요?"
    elif emotion_detected == "짜증":
        return "짜증 날 땐 충동구매도 하게 되죠. 지금 마음은 좀 괜찮으세요?"
    elif emotion_detected == "기쁨":
        return "기분 좋을 때의 소비는 즐겁죠. 만족스러웠나요?"
    else:
        return "오늘 어떤 소비를 하셨고, 기분은 어떠셨나요?"

@app.post("/chat")
def chat(msg: Message):
    user_input = msg.message
    reply = analyze_message(user_input)
    return {"response": reply}
