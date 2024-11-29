from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.users     import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )
    
    decoded_token = verify_access_token(token)
    return decoded_token["user"]