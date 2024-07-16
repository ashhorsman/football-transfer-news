import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import Navbar from './components/Navbar';

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/accounts/login/" element={<LoginPage />} />
                <Route path="/accounts/signup/" element={<SignupPage />} />
            </Routes>
        </Router>
    );
}

export default App;
