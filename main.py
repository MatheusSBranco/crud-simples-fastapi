from fastapi import FastAPI

from src.module import controller

app = FastAPI()

app.include_router(controller.controller)

@app.get("/")
def root():
    return {"message": "Hello"}