
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import EmotionDiary from './EmotionDiary';

export default function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<EmotionDiary />} />
      </Routes>
    </Router>
  );
}
