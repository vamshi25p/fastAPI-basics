from .. import models,schemas,hashing 
from fastapi import HTTPException,status 
from sqlalchemy.orm import Session 

def create_user(request:schemas.User,db:Session): 
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id:int,db:Session): 
    user=db.query(models.User).filter(models.User.id==id).first() 
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found") 
    return user
def get_all_users(db:Session):
    users=db.query(models.User).all() 
    return users   

