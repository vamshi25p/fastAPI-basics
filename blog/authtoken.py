from typing import Optional
from jose import jwt,JWTError
from datetime import datetime,timedelta
from fastapi import Depends
from blog.schemas import TokenData

SECRET_KEY="1hbschdwqg82u2hvwvjw1vwy1wb1uwkh1u9hh1wbo1ijwi1ui1"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30 

def create_access_token(data:dict,expires_delta:Optional[timedelta]=None): 
    to_encode=data.copy() 
    if expires_delta: 
        expire=datetime.utcnow() + expires_delta 
    else: 
        expire=datetime.utcnow()+timedelta(minutes=15) 

    to_encode.update({"exp":expire}) 

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) 
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get("sub")
        if email is None: 
            raise credentials_exception 
        token_data=TokenData(email=email)
    except JWTError: 
        raise credentials_exception