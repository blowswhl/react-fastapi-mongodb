import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';
import DevelopMain from './pages/Developmain';
import InfraMain from './pages/Inframain';
import NoticeInfra from './pages/Notice';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/SignUpPage" element={<SignUpPage />} />
        <Route path="/DevelopMain" element={<DevelopMain />} />
        <Route path="/InfraMain" element={<InfraMain />} />
        <Route path="/NoticeInfra" element={<NoticeInfra />} />

  
      </Routes>
    </Router>
  );
}

export default App;
