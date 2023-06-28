from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "SatyaDev"}

@app.get("/satya")
def read_root():
    return {"Hello": "Satya"}
