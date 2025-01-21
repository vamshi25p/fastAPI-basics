from fastapi import APIRouter,Depends,Response,status,HTTPException

from typing import List 
from .. import schemas,models,hashing
from sqlalchemy.orm import Session 
from ..database import engine,SessionLocal,get_db
from ..repository import user
from ..oauth2 import get_current_user
router=APIRouter(
    tags=['Users'],
    prefix='/user'
)


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return user.create_user(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowUser)
def get_user(id:int,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)): 
    return user.get_user(id,db)

@router.get('/',response_model=List[schemas.ShowUser])
def get_all_users(db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)): 
    return user.get_all_users(db)  

