from fastapi import FastAPI

greeting = FastAPI()


@greeting.get("/")
async def root():
    return {"message": "Hello World"}
