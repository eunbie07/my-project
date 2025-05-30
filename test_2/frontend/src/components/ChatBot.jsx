import { useState } from "react";
import axios from "axios";

export default function ChatBot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { from: "user", text: input }];
    setMessages(newMessages);
    setInput("");

    try {
      const res = await axios.post("http://localhost:3000/chat", {
        message: input,
      });

      setMessages([...newMessages, { from: "bot", text: res.data.response }]);
    } catch {
      setMessages([
        ...newMessages,
        { from: "bot", text: "서버 오류가 발생했어요." },
      ]);
    }
  };

  return (
    <div className="bg-[#f2ebfa] min-h-screen flex items-center justify-center">
      <div className="bg-white rounded-3xl shadow-lg p-5 w-[360px] h-[640px] flex flex-col relative">
        {/* 상단 헤더 */}
        <div className="flex items-center gap-2 justify-center py-3 bg-gradient-to-r from-lime-200 to-emerald-300 rounded-2xl w-fit mx-auto mb-3 px-4 shadow">
          <img src="/chatbot.png" alt="챗봇" className="w-6 h-6" />
          <h1 className="text-white text-sm font-semibold tracking-wide">
            리마인봇과 함께하는 소비 반성 챗봇
          </h1>
        </div>

        {/* 메시지 목록 */}
        <div className="flex-1 overflow-y-auto px-1 py-1 space-y-2 mb-2">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex ${
                msg.from === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`rounded-3xl px-4 py-2 max-w-[75%] text-sm shadow-sm ${
                  msg.from === "user"
                    ? "bg-purple-200 text-right"
                    : "bg-emerald-100 text-left"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}
        </div>

        {/* 하단 챗봇 아이콘 */}
        <div className="flex justify-center my-2">
          <img
            src="/chatbot.png"
            alt="챗봇"
            className="w-6 h-6 opacity-50 animate-bounce"
          />
        </div>

        {/* 입력창 */}
        <div className="flex mt-auto">
          <input
            className="flex-1 border border-gray-300 rounded-full px-4 py-2 text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-300 transition"
            placeholder="오늘 있었던 소비를 이야기해보세요..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button
            onClick={sendMessage}
            className="ml-2 bg-gradient-to-r from-purple-400 to-purple-500 text-white px-5 py-2 rounded-full shadow-md hover:opacity-90 transition"
          >
            보내기
          </button>
        </div>
      </div>
    </div>
  );
}
