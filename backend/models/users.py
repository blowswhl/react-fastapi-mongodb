from pydantic import BaseModel,Field
from typing import List 
from beanie import Document
from passlib.context import CryptContext
from jose import jwt, JWTError 
from datetime import  datetime,timedelta, timezone
from typing import Optional
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "023387806201433c7686993ffc161ae49cfa7fa1cd6d615fd71c4c1f4b917613"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





#mongodb와 fastapi 연동하기위한 모델
#Document를 상속받아 Beanie ODM 을 사용해 MongoDB문서와 매핑
class User(Document):
    username: str = Field(..., unique=True)
    hashed_password: str
    email: str
    team: str = []
    tags: List[str] = []
    secret_key: str = "test123"
    jwt_algorithm = "HS256"

    class Config:
        schema_extra = {
            "example": {
                "username": "admin",
                "password": "1234",
                "email": "admin@exaample.com",
                "team": "인프라팀",
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
    
    def create_access_token(self, username: str) -> str:
        expiration = datetime.utcnow() + timedelta(days=1)  # UTC 사용 권장
        payload = {
            "user": username,  # 유니크한 식별자
            "exp": expiration,  # 만료 시간
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.jwt_algorithm)

    
     # JWT 토큰 검증 User안에 있을필요가 없음 나중에 수정해야함 
    @staticmethod
    def verify_access_token(token: str, secret_key: str) -> Optional[dict]:
        try:
            # 토큰 디코딩
             # 토큰과 시크릿 키, 알고리즘 출력
            print(f"Token: {token}")
            print(f"Secret Key: {secret_key}")
            print(f"Algorithm: HS256")
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            print(f"Decoded Data: {data}")
            return data  # 유효한 경우 디코딩된 데이터 반환
        except jwt.ExpiredSignatureError:
            print("토큰이 만료되었습니다.")
            return None
        except JWTError:  # jwt.InvalidTokenError 대신 사용
            print("유효하지 않은 토큰입니다.")
            return None
        


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str
    team: str