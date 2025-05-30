# 1. 가상환경 설정 (선택)
python -m venv .venv
source .venv/bin/activate  # 윈도우는 .venv\Scripts\activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. Ollama 실행 (별도 터미널에서)
ollama run llama3

# 4. FastAPI 서버 실행
uvicorn main:app --reload --port 3000
