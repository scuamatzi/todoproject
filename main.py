from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

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
    #return {"ping":"pong"}
    return "Hello World!"

@app.get("/api/todo")
async def get_todo():
    return "ok"

@app.get("/api/todo/{id}")
async def get_todo_by_id(id):
    return "ok"

@app.post("/api/todo")
async def post_todo(todo):
    return "ok"

@app.put("/api/todo/{id}")
async def update_todo(id, data):
    return "ok"

@app.delete("/api/todo/{id}")
async def delete_todo(id):
    return "ok"