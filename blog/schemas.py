from pydantic import BaseModel
from typing import List,Optional

class Blog(BaseModel): 
    title:str
    body:str 
    class Config(): 
        from_attributes=True 




class User(BaseModel): 
    name:str 
    email:str 
    password:str 



class ShowUser(BaseModel): 
    name: str
    email: str
    blogs: List[Blog]  # Assuming the user has a list of blogs

class ShowBlog(BaseModel): 
    title: str
    body: str
    creator: ShowUser


class Login(BaseModel): 
    username:str
    password:str


class Token(BaseModel): 
    access_token:str 
    token_type:str 

class TokenData(BaseModel): 
    email: Optional[str]=None 

