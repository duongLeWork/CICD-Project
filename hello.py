from fastapi import FastAPI

app = FastAPI()


@app.get("/a")
async def root():
    return {"message": "Hello World"}
