import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import './LoginPage.css'; //스타일추가
//리액트 코드를 작성할떄 필수적으로 리액트를 가져와야함
// React 17 이상에서는 자동으로 JSX를 처리하지만, 명시적으로 import React를 사용하는 것이 관례적입니다.


//const 재변경 불가능 상수같은의미
//리액트 컴포넌트로 작동한다.
const LoginPage = () => {
    //id password저장하는거 선언 = 초기는 빈값 
    //set애들이 상태를 실시간으로 전달받아 값을바꿔줌 
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    //로그인폼버튼누를시 호출 
    const handleLogin = async (e) => {
        e.preventDefault(); // 폼 제출 기본 동작 방지

        try {
            const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
            //백엔드 fastapi서버로 요청을보냄 json형식으로 보냄 
                // Form 데이터를 URL 인코딩 형식으로 변환
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', password);

            const response = await fetch(`${backendUrl}/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData.toString(),
                credentials: 'include',  // 쿠키를 포함한 요청을 허용
            });
                //Http 응답 반환을 통해 200대일시 
                // data에 담긴 팀이 개발 이나 인프라일시 해당페이지이동 
                //===쓰는이유는 ==일시 형변환일어날수있음 === 두값과 타입까지
                // '5' == 5 는 5==5 가됨 
            if (response.ok) {
                const data = await response.json();
                
                alert(`로그인 성공: ${data.message}`);
                if (data.team === '개발') {
                    navigate('/DevelopMain');
                
                } else if (data.team === '인프라') {
                    navigate('/Inframain');
                }

            } else {
                const error = await response.json();
                alert(`로그인 실패: ${error.detail}`);
            }
        } catch (err) {
            alert(`에러 발생: ${err.message}`);
        }
    };
    //return은 React 컴포넌트가 화면에 표시할 JSX를 반환하는부분
    //리액트는 이 return 값을 사용해 브라우저 DOM에 렌더링합니다.
    //리액트 컴포넌트는 반드시 반환값을 가져야함
    return (
        <div className='login-container'>
         <div className='login-box'>
            <h1>로그인 페이지!</h1>
            <form onSubmit={handleLogin}>
                <input type="text" placeholder="아이디"  value={username}
        onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="비밀번호" value={password}
        onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">로그인</button> 
            </form>
                {/* 하이퍼링크 추가 */}
                <div className="links">
                <a href="/find-id">아이디 찾기</a>
                <a href="/find-password">비밀번호 찾기</a>
                <a href="/SignUpPage">회원가입</a>
                </div>
            </div>

        </div>
    );
};
/*
placeholder는 기본값과는 약간 다릅니다. placeholder는 입력 필드에 표시되는 힌트 텍스트로, 
사용자가 입력을 시작하기 전까지 입력 필드에 나타나는 설명 텍스트입니다. 기본값처럼 실제 값으로 취급되지는 않으며, 사용자가 텍스트를 입력하면 사라집니다.
*/

export default LoginPage;
