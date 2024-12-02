from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings
from models.users import User
from models.Notice import Notice,Notice2,Notice3,Notice4

#몽고db 데이터베이스 초기화 영역 모델들 추가시켜줘야 같이 초기화되면서
#해당모델들이 몽고db랑 연결됨 

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = None
    

    class Config:
         env_file = ".env"

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),document_models=[User, Notice, Notice2, Notice3,Notice4]) #유저모델 db랑 연결 



class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return
    
    