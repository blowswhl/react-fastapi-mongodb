import time
from datetime import datetime, timezone

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

Settings = Settings()

def create_access_token(user: str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }

    token = jwt.encode(payload, Settings.SECRET_KEY, algorithm="HS256")
    return token


def verify_access_toekn(token: str):
    try:
        data = jwt.decode(token, Settings.SECRET_KEY, algorithms=["HS256"])

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        if datetime.now(timezone.utc) > datetime.fromtimestamp(expire, tz=timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )
