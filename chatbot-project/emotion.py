
def analyze_emotion(text):
    if "짜증" in text or "화나" in text:
        return "분노"
    elif "우울" in text or "속상" in text:
        return "우울"
    elif "기뻐" in text or "좋아" in text:
        return "행복"
    elif "불안" in text or "걱정" in text:
        return "불안"
    else:
        return "중립"
