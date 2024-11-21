from fastapi import APIRouter, HTTPException, status
from models.users import User,LoginRequest, RegisterRequest

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
@user_router.post("/login")
async def login(request: LoginRequest):
    user = await User.find_one(User.username == request.username)
    if user and user.verify_password(request.password):
        return {"message": "로그인 성공!"}
    raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 올바르지 않습니다.")

#회원가입 라우터 username을기준으로

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
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
        hashed_password=""  # 초기값 설정
    )
    await user.set_password(request.password)  # 비밀번호 해싱
    await user.insert()  # MongoDB에 저장
    
    return {"message": "User registered successfully"}
