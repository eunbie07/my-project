def analyze_emotion(text):
    if any(word in text for word in ["짜증", "화나", "열받"]):
        return "분노"
    elif any(word in text for word in ["우울", "속상", "눈물"]):
        return "우울"
    elif any(word in text for word in ["기뻐", "좋아", "행복", "기분 좋"]):
        return "행복"
    elif any(word in text for word in ["불안", "걱정", "초조", "찝찝"]):
        return "불안"
    else:
        return "중립"
