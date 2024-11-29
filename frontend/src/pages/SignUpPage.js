import React, { useState } from "react";
import "./SignUpPage.css"; // CSS 파일을 별도로 추가

const SignUpPage = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [selectedTeam, setSelectedTeam] = useState("인프라");

    const teams = ["인프라", "개발"];

    const handleSubmit = async (e) => {
        e.preventDefault();
        const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
        const userData = { username, password, email, team: selectedTeam };
        try {
            const response = await fetch(`${backendUrl}/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(userData),
            });

            if (response.ok) {
                const data = await response.json();
                alert("회원가입 성공: " + data.message);
            } else {
                const errorData = await response.json();
                alert("회원가입 실패: " + errorData.message);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("서버와 통신 중 오류가 발생했습니다.");
        }
    };

    return (
        <div className="SignUpPage">
            <div className="form-container">
                <h2>회원가입</h2>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="아이디"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <input
                        type="password"
                        placeholder="비밀번호"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <input
                        type="email"
                        placeholder="이메일"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <div className="team-select">
                        팀선택:   
                        <select
                            value={selectedTeam}
                            onChange={(e) => setSelectedTeam(e.target.value)}
                        >    
                            {teams.map((team) => (
                                <option key={team} value={team}>
                                    {team}
                                </option>
                            ))}
                        </select>
                    </div>
                    <button type="submit">회원가입</button>
                </form>
            </div>
        </div>
    );
};

export default SignUpPage;
