#fastapi imports
from fastapi import FastAPI
app = FastAPI()

#basic imports
import constants


@app.get(constants.root)
async def root():
    return {"message": "Hello, I am Om Prakash"}
