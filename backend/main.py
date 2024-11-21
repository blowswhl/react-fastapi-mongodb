from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from database.connection import Settings

app = FastAPI()

# CORS 설정 리액트
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

settings = Settings()
# mongoDB연결 설정 
@app.on_event("startup")
async def on_startup():
  await settings.initialize_database()

#기본경로
@app.get("/")
async def welcome() -> dict:
    return {
             "message": "Hello World"
    }

app.include_router(user_router)