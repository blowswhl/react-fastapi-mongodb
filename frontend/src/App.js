import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';
import DevelopMain from './pages/Developmain';
import InfraMain from './pages/Inframain';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/SignUpPage" element={<SignUpPage />} />
        <Route path="/DevelopMain" element={<DevelopMain/>} />"
        <Route path="/InfraMain" element={<InfraMain/>} />"
      </Routes>
    </Router>
  );
}

export default App;
