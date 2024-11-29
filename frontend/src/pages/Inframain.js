import React, { useEffect,useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Carousel from 'react-bootstrap/Carousel';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import 'bootstrap/dist/css/bootstrap.min.css';
import FristImage from './images/InfraFrist.jpg';
import SecondImage from './images/InfraSecond.jpg';
import ThreeImage from './images/InfraThree.jpg';
import axios from 'axios'; // axios 추가

// 샘플 데이터
const notices = [
  "공지사항 1",
  "공지사항 2",
  "공지사항 3",
  "공지사항 4",
  "공지사항 5",
];

const requests = [
  "요청사항 1",
  "요청사항 2",
  "요청사항 3",
  "요청사항 4",
  "요청사항 5",
];

// 네비게이션 바 컴포넌트
function ColorSchemesExample() {
  return (
    <Navbar bg="primary" data-bs-theme="dark" fixed="top" style={{ height: '80px' }}>
      <Container>
        <Navbar.Brand href="#home" style={{ fontSize: '1.5rem', color: '#ffffff' }}>
          인프라팀
        </Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href="/NoticeInfra" style={{ fontSize: '1.2rem', color: '#ffffff' }}>
            공지사항
          </Nav.Link>
          <Nav.Link href="#프로젝트관리" style={{ fontSize: '1.2rem', color: '#ffffff' }}>
            리소스 요청사항
          </Nav.Link>
          <Nav.Link href="#자료실" style={{ fontSize: '1.2rem', color: '#ffffff' }}>
            자료실
          </Nav.Link>
          <Nav.Link href="#개발도구" style={{ fontSize: '1.2rem', color: '#ffffff' }}>
            고객사 현황
          </Nav.Link>
          <Nav.Link href="#일정회의" style={{ fontSize: '1.2rem', color: '#ffffff' }}>
            일정 및 회의
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

// 캐러셀 컴포넌트
function UncontrolledExample() {
  return (
    <Carousel>
      <Carousel.Item>
        <img className="d-block w-100" src={FristImage} alt="First slide" />
        <Carousel.Caption>
          <h3>11월 서버작업일정</h3>
          <p>인프라팀분들 확인 바랍니다.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img className="d-block w-100" src={SecondImage} alt="Second slide" />
        <Carousel.Caption>
          <h3>12월 서버작업일정</h3>
          <p>인프라팀분들 확인 바랍니다.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img className="d-block w-100" src={ThreeImage} alt="Third slide" />
        <Carousel.Caption>
          <h3>1월 서버작업일정</h3>
          <p>인프라팀분들 확인 바랍니다.</p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}

// 최신 글 섹션
function LatestUpdates() {
  return (
    <Container style={{ marginTop: '20px' }}>
      <Row>
        {/* 공지사항 섹션 */}
        <Col>
          <h4 style={{ marginBottom: '15px' }}>공지사항</h4>
          <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
            {notices.map((notice, index) => (
              <li key={index} style={{ marginBottom: '5px' }}>
                {notice}
              </li>
            ))}
          </ul>
        </Col>

        {/* 요청사항 섹션 */}
        <Col>
          <h4 style={{ marginBottom: '15px' }}>리소스 요청사항</h4>
          <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
            {requests.map((request, index) => (
              <li key={index} style={{ marginBottom: '5px' }}>
                {request}
              </li>
            ))}
          </ul>
        </Col>
      </Row>
    </Container>
  );
}
function InfraMain() {
    const navigate = useNavigate();
    
  
    return (
      <>
        {/* 네비게이션 바 */}
        <ColorSchemesExample />
  
        {/* 네비게이션 바 높이만큼 공백 추가 */}
        <div style={{ height: '80px', backgroundColor: 'lightgray' }}></div>
  
        {/* 캐러셀 및 콘텐츠 */}
        <div style={{ backgroundColor: '#f9f9f9', minHeight: '100vh', padding: '20px' }}>
          {/* 캐러셀 */}
          <UncontrolledExample />
  
          {/* 공지사항 및 요청사항 */}
          <LatestUpdates />
        </div>
      </>
    );
  }
  
  
  export default InfraMain;
