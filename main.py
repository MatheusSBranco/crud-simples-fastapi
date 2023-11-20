from fastapi import FastAPI

from src.module import router

app = FastAPI()

app.include_router(router.router)

@app.get("/")
def root():
    return {"message": "Hello"}