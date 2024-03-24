from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Ada": "TVADUMBCHYTVAREC"}


@app.get("/ping")
def read_ping():
    return {"ping": "pong"}
