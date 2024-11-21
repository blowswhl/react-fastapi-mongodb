import React from 'react';
import './LoginPage.css'; //스타일추가
//리액트 코드를 작성할떄 필수적으로 리액트를 가져와야함
// React 17 이상에서는 자동으로 JSX를 처리하지만, 명시적으로 import React를 사용하는 것이 관례적입니다.


//const 재변경 불가능 상수같은의미
//리액트 컴포넌트로 작동한다.
const LoginPage = () => {
    //return은 React 컴포넌트가 화면에 표시할 JSX를 반환하는부분
    //리액트는 이 return 값을 사용해 브라우저 DOM에 렌더링합니다.
    //리액트 컴포넌트는 반드시 반환값을 가져야함
    return (
        <div className='login-container'>
         <div className='login-box'>
            <h1>로그인 페이지</h1>
            <form>
                <input type="text" placeholder="아이디" />
                <input type="password" placeholder="비밀번호" />
                <button type="submit">로그인</button> 
            </form>
                {/* 하이퍼링크 추가 */}
                <div className="links">
                <a href="/find-id">아이디 찾기</a>
                <a href="/find-password">비밀번호 찾기</a>
                <a href="/signup">회원가입</a>
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
