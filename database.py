from model import Todo
import motor.motor_asyncio

client=motor.motor_asyncio.AsyncIOMotorClient("mongodb://user:password@localhost")