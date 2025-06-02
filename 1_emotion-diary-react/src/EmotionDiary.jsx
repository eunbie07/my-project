
import React, { useState, useEffect } from 'react';

export default function EmotionDiary() {
  const [sessionId, setSessionId] = useState('test123');
  const [emotion, setEmotion] = useState('우울');
  const [text, setText] = useState('지친 하루였어');
  const [entries, setEntries] = useState([]);

  const writeDiary = async () => {
    await fetch(`/diary/write?session_id=${sessionId}&emotion=${emotion}&text=${encodeURIComponent(text)}`, {
      method: 'POST'
    });
    fetchEntries();
  };

  const fetchEntries = async () => {
    const res = await fetch(`/diary/list?session_id=${sessionId}`);
    const data = await res.json();
    setEntries(data);
  };

  const generateAIImage = async () => {
    await fetch(`/diary/generate_ai_image?session_id=${sessionId}`);
    fetchEntries();
  };

  const downloadPDF = () => {
    window.open(`/report/pdf-full?session_id=${sessionId}`);
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  return (
    <div className="p-6 space-y-4 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold">감정 그림 일기</h1>

      <div className="space-y-2">
        <input value={sessionId} onChange={e => setSessionId(e.target.value)} className="border p-2 w-full" placeholder="세션 ID" />
        <select value={emotion} onChange={e => setEmotion(e.target.value)} className="border p-2 w-full">
          <option>기쁨</option>
          <option>우울</option>
          <option>짜증</option>
          <option>힐링</option>
          <option>중립</option>
        </select>
        <input value={text} onChange={e => setText(e.target.value)} className="border p-2 w-full" placeholder="한 줄 일기" />
        <button onClick={writeDiary} className="bg-blue-500 text-white px-4 py-2 rounded">일기 저장</button>
        <button onClick={generateAIImage} className="bg-green-500 text-white px-4 py-2 rounded">AI 그림 생성</button>
        <button onClick={downloadPDF} className="bg-purple-500 text-white px-4 py-2 rounded">PDF 리포트</button>
      </div>

      <h2 className="text-xl mt-6">🖼️ 그림 일기</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {entries.map(entry => (
          <div key={entry._id} className="border p-4 rounded shadow">
            <p><strong>감정:</strong> {entry.emotion}</p>
            <p className="mb-2">“{entry.text}”</p>
            <img
              src={`/diary/generate_image?session_id=${entry.session_id}&ts=${entry._id}`}
              alt="일기 이미지"
              className="w-full mb-2"
            />
            <a
              href={`/diary/generate_image?session_id=${entry.session_id}&ts=${entry._id}`}
              download={`diary_${entry._id}.png`}
              className="bg-gray-600 text-white px-3 py-1 rounded"
            >이미지 다운로드</a>
          </div>
        ))}
      </div>
    </div>
  );
}
