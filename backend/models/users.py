from pydantic import BaseModel,Field
from typing import List 
from beanie import Document
from passlib.context import CryptContext
 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#mongodb와 fastapi 연동하기위한 모델
#Document를 상속받아 Beanie ODM 을 사용해 MongoDB문서와 매핑
class User(Document):
    username: str = Field(..., unique=True)
    hashed_password: str
    email: str
    tags: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "1234",
                "email": "admin@exaample.com",
                "tags": ["admin", "user"]
            }
        }
    #이 모델이 MongoDB의 users 컬렉션과 연결될것을 지정
    class Settings:
        name = "users"

    #비밀번호관련 인코딩하고 소금생성 소금 동일한 비번이라도 다른 해시값을 생기게 
    #bcrypt는 해시값에 소금정보를 포함하고있어 해시값만으로도 검증가능 
    async def set_password(self, raw_password: str):
        self.hashed_password = pwd_context.hash(raw_password)
    #디코딩하여 저장된비밀번호가 일치하는지 비교 
    def verify_password(self, raw_password: str) -> bool:
        return pwd_context.verify(raw_password, self.hashed_password)    

class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str 