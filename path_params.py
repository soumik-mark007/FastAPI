from fastapi import FastAPI, HTTPException
from enum import Enum
app = FastAPI()

class RoleChoices(Enum):
    ds = "DS"
    sds = "SDS"
    lds = "LDS"


BANDS = [

    {"id":"1","name":"Soumik","role":"DS"},
    {"id":"2","name":"Piyush" , "role":"SDS"},
    {"id":"3","name":"Pranjal", "role":"DS"},
    {"id":"4","name":"Anupam", "role":"LDS"}
]

@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get("/bands/{band_id}")
async def read_item(band_id: str) -> str:
    band = next((b["name"] for b in BANDS if b["id"] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404, detail="band not found")
    return band

@app.get("/bands/roles/{role}")
async def genre(role : RoleChoices) -> list[dict]:
    result = [
        next((b for b in BANDS if b["role"]==role.value), None)
    ]
    if result is None:
        raise HTTPException(status_code=404,detail="role not found")
    return result
