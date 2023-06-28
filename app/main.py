from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "SatyaDev"}

@app.get("/sri")
def read_root():
    return {"Hello": "Sri"}
    
@app.get("/satya")
def read_root():
    return {"Hello": "Satya"}
    
@app.get("/dev")
def read_root():
    return {"Hello": "Dev"}


