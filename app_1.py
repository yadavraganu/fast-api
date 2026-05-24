from fastapi import FastAPI

app_1 = FastAPI()

@app_1.get("/")
async def root():
    return {"message": "Hello World"}