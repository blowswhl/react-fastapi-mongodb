from fastapi import FastAPI
from fastapi import HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.users import user_router
from routes.Notice import notice_router
from routes.DevNotice import Dev_notice_router
from database.connection import Settings

app = FastAPI()

# CORS 설정 리액트
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://211.183.3.241", "http://211.183.3.222:3100", "http://211.183.3.241:3100", "http://211.183.3.203","http://211.183.3.203:3100"],  # React 개발 서버 주소
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
app.include_router(notice_router)
app.include_router(Dev_notice_router)