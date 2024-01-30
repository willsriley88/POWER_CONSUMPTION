from fastapi import FastAPI
from routers import voltage_post

app = FastAPI()


app.include_router(voltage_post.router)


@app.get("/")
def root():
    return {"data": "home"}







