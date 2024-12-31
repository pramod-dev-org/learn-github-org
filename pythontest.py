from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
import base64
import os

app = FastAPI()

class TextItem(BaseModel):
    text: str

@app.post("/checksum/")
async def create_checksum(item: TextItem):
    if not item.text:
        raise HTTPException(status_code=400, detail="Text field is required")
    checksum = hashlib.md5(item.text.encode()).hexdigest()
    return {"checksum": checksum}