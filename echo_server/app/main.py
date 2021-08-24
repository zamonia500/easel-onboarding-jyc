from fastapi import FastAPI

from .routers import echo

app = FastAPI()


app.include_router(echo.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
