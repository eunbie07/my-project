from langchain.memory import ConversationBufferMemory

# 메모리 생성
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("배고프다")
memory.chat_memory.add_ai_message("어디 가서 밥 먹을까?")
memory.chat_memory.add_user_message("라면 먹으러 가자")
memory.chat_memory.add_ai_message("지하철역 앞에 있는 분식집으로 가자")
memory.chat_memory.add_user_message("그럼 출발!")
memory.chat_memory.add_ai_message("OK!")

# 메모리 변수 가져오기
print(memory.load_memory_variables({}))
