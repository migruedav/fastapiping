from fastapi import FastAPI
from sel import sel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Ada": "TVADUMBCHYTVAREC"}


@app.get("/ping")
def read_ping():
    return {"ping": "pong"}


@app.get("/sel")
def read_sel():
    return sel()
