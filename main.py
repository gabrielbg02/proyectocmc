
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hola": "mundo"}

@app.get("/test")
async def read_root():
    return {"prueba": "probando"}
