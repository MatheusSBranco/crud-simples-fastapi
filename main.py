from fastapi import FastAPI

from src.module.controller.book import controller

app = FastAPI()

app.include_router(controller)

@app.get("/")
def root():
    return {"message": "Hello"}