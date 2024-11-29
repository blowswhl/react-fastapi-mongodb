# 1. Node.js 이미지를 기반으로 설정
FROM node

# 2. 작업 디렉토리 생성
WORKDIR /project/frontend

# 3. package.json 및 package-lock.json을 복사하여 의존성 설치
COPY package.json package-lock.json ./

# 4. 의존성 설치
RUN npm install

# 5. 나머지 소스 파일 복사
COPY ./ /project/frontend

# 6. 컨테이너의 3000번 포트 노출
EXPOSE 3000

# 7. npm start로 리액트 애플리케이션 실행
CMD ["npm", "start"]