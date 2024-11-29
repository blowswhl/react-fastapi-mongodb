import React, { useState, useEffect } from 'react';

// 게시글 데이터 예시
const dummyPosts = [
  { id: 1, title: '첫 번째 글 제목' },
  { id: 2, title: '두 번째 글 제목' },
  { id: 3, title: '세 번째 글 제목' },
  { id: 4, title: '네 번째 글 제목' },
  { id: 5, title: '다섯 번째 글 제목' },
  { id: 6, title: '여섯 번째 글 제목' },
  { id: 7, title: '일곱 번째 글 제목' },
  { id: 8, title: '여덟 번째 글 제목' },
  { id: 9, title: '아홉 번째 글 제목' },
  { id: 10, title: '열 번째 글 제목' },
];

const NoticeInfra = () => {
  const [posts, setPosts] = useState([]);

  // 게시글 데이터를 로드하는 useEffect 예시 (데이터가 API에서 불러와지는 경우)
  useEffect(() => {
    // 여기서는 dummy 데이터를 상태에 설정합니다.
    setPosts(dummyPosts);
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>공지사항</h1>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {posts.map((post) => (
          <li key={post.id} style={{ marginBottom: '10px', padding: '10px', borderBottom: '1px solid #ddd' }}>
            <h2 style={{ margin: '0' }}>{post.title}</h2>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NoticeInfra;
