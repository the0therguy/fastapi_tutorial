from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10):
    return {"data": f"{limit} blog list"}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': "all the unpublished data"}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comment(id: int):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"blog is created with title as {blog.title}"}
