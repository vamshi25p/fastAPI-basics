from fastapi import APIRouter,Depends,HTTPException,status 
from .. import schemas,database,models,hashing
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from ..authtoken import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(
    tags=['Authentication']
) 


@router.post('/login') 
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)): 
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not hashing.Hash.verify(user.password,request.password): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    

    access_token=create_access_token(
        data={"sub":user.email}
    )

    return {"access_token":access_token,"token_type":"bearer"}