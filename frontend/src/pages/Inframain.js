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


// 샘플 데이터


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
function LatestUpdates({ notices , notices2 }) {
      
    const noticesList = notices || [];
    const noticesList2 = notices2 || [];
    console.log(notices2);
  
  
  return (
    <Container style={{ marginTop: '20px' }}>
      <Row>
        {/* 공지사항 섹션 */}
        <Col>
          <h4 style={{ marginBottom: '15px' }}>공지사항</h4>
          <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
            {noticesList.length > 0 ? (
              noticesList.map((notice, index) => (
                <li key={index} style={{ marginBottom: '5px'}}>
                  {notice.title}
                </li>
              ))
            ) : (
              <li>등록된 공지사항이 없습니다.</li>
            )}
          
          </ul>
        </Col>

        {/* 요청사항 섹션 */}
        <Col>
          <h4 style={{ marginBottom: '15px' }}>리소스 요청사항</h4>
          <ul style={{ listStyleType: 'none', paddingLeft: '0' }}> 
            {noticesList2.length > 0 ? (
              noticesList2.map((notice, index) => (
                <li key={index} style={{ marginBottom: '5px' }}>
                  {notice.title}
                </li>
              ))
            ) : (
              <li>등록된 리소스 요청사항이 없습니다.</li> // 데이터가 없을 경우 표시할 문구
            )}
          </ul>
        </Col>
      </Row>
    </Container>
  );
}


function InfraMain() {
  const navigate = useNavigate();
  const [notices, setNotices] = useState([]); // 공지사항 상태 추가
  const [loading, setLoading] = useState(true); // 로딩 상태
  const [error, setError] = useState(null); // 오류 상태
  const [notices2, setNotices2] = useState([]); // 공지사항 상태 추가
 

  useEffect(() => {
      const fetchNotices = async () => {
          try {
              const response = await fetch('http://localhost:8000/Notices'); // FastAPI 서버에서 공지사항 데이터 요청
              const response2 = await fetch('http://localhost:8000/Notices2');
              const data = await response.json();
              const data2 = await response2.json();
              console.log(data2);
              
              setNotices(data); // 가져온 데이터를 상태에 저장
              setNotices2(data2);
          } catch (error) {
              console.error('Error fetching notices:', error); // 오류 처리
              setError('공지사항을 가져오는 데 실패했습니다.');
          } finally {
              setLoading(false); // 로딩 완료
          }
      };

      fetchNotices();
  }, []); // 이 부분이 빈 배열로 설정되어 있어 페이지가 로드될 때만 실행됨

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

              {/* 로딩 상태 처리 이거 없으면 빈값이 넘어가서 공지사항없음출력됨 데이터가져오기전에
              로딩되서 출력이됨 */}
              {loading ? (
                  <div>로딩 중...</div> 
              ) : (
                  // 공지사항 데이터가 로딩된 후에만 LatestUpdates 렌더링
                  <LatestUpdates notices={notices} notices2={notices2} />
              )}
          </div>
      </>
  );
}
  
  
  export default InfraMain;
