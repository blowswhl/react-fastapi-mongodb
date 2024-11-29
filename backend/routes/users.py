from fastapi import APIRouter, HTTPException, status, Depends, Response, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models.users     import User
from models.users import User,LoginRequest, RegisterRequest
from jose import jwt, JWTError, ExpiredSignatureError
from models.jwt_handler import create_access_token,verify_access_toekn

user_router = APIRouter(
    tags=["User"],
)

users= {}

# @user_router.post("/login")
# async def login(request: LoginRequest):
#     if request.username == "admin" and request.password == "1234":
#         return {"message": "로그인 성공!"}
#     raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 올바르지 않습니다.")

#몽고 db에서 특정사용자를 찾는 역할 await User.find_one
#user가 user패스워드 일치하는지 검증 
#로그인 라우터
# 모든 사용자 목록 조회
@user_router.get("/users")
async def get_users():
    users = await User.find_all().to_list()  # MongoDB에서 모든 사용자 조회
    return {"users": users}

@user_router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), response: Response = None):
    user = await User.find_one(User.username == request.username)
    if user and user.verify_password(request.password):
        access_token: str = create_access_token(user.username)
        
        # 로그인 성공 시, 쿠키에 JWT 토큰 저장
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,  # JavaScript에서 접근 불가
            secure=False,    # HTTPS에서만 쿠키 전송 (배포 환경에서는 True 설정)     # 만료시간
            path="/"        # 쿠키가 적용되는 경로
        )
        
        # 응답 본문에 사용자 정보 반환
        return {
             "message": f"로그인 성공! {access_token}",
            "team": user.team
        }
    else:
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 올바르지 않습니다.")
  
#회원가입 라우터 username을기준으로
@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    print(request.dict())
    print(request.team)
    # 사용자 이름 중복 확인
    existing_user = await User.find_one(User.username == request.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # 이메일 중복 확인
    existing_email = await User.find_one(User.email == request.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # 사용자 생성 및 비밀번호 해싱
    user = User(
        username=request.username,
        email=request.email,
        hashed_password="",  # 초기값 설정
        team=request.team,
        
    )
    await user.set_password(request.password)  # 비밀번호 해싱
    await user.insert()  # MongoDB에 저장
    
    return {"message": "User registered successfully"}

@user_router.get("/api/verify-token")
async def verify_token(request: Request):
    token = request.cookies.get("access_token")
    print("Received token:", token)
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        user_data = verify_access_toekn(token)
        if user_data is None:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    print("Token is valid")  # 로그 출력
    return {"message": "Token is valid", "user_data": user_data}


#서버에서 토큰검증


#회원정보 수정 만들어야함 


#회원탈퇴 만들어야함 