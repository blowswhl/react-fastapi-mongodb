# backend/Dockerfile

FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /project/backend

# 종속성 파일 복사 및 설치
COPY requirements.txt /project/backend/requirements.txt
RUN pip install --upgrade pip && pip install -r /project/backend/requirements.txt

EXPOSE 8000

# 애플리케이션 코드 복사
COPY ./ /project/backend

# 애플리케이션 시작 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

