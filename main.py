from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI() #instance 


#path operation decorator
@app.get('/blog')  #path
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}  #path operation function
    else:
        return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id=id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int,limit=100):
    return {"data":['1','2']}


class Blog(BaseModel):
    title:str 
    body:str 
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with {blog.title}"}


#if __name__=="__main__":
#    uvicorn.run(app,host="127.0.0.1",port='9000')

