from model import Todo
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient("mongodb://user:password@localhost")

database=client.TodoList
collection=database.todo

async def fetch_one_todo(title):
    document=await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos=[]
    cursor=collection.find({})
    async for item in cursor:
        todos.append(Todo(**item))
    return todos

async def create_todo(todo):
    item=todo
    result= await collection.insert_one(item)
    return item

async def update_todo(title,desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}})
    item = await collection.find_one({"title":title})
    return item

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True