from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app=FastAPI()
templates=Jinja2Templates(directory="templates")

from database import(
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)

#CORS allows to anser request from "other" resources.
#In this case port 3000 is to answer requests from REACT
origins=['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def index():
    return "Hello World!"

@app.get("/api/todo",response_model=list[Todo])
async def get_todo(request:Request):
    response = await fetch_all_todos()
    #return response
    return templates.TemplateResponse("inicio.html",{"request":request ,"listado":response})

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=404,detail=f"There is no TODO item with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(status_code=404, detail="Bad request")

@app.put("/api/todo/{id}", response_model=Todo)
async def update_todo_item(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(status_code=404,detail=f"There is no TODO item with this title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title:str):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo item! "
    raise HTTPException(status_code=404, detail=f"There is no TODO item with this {title}")