from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str,str]:
    return {"hello":"world"}


@app.get("/about")
async def abount() -> str:
    return "response from about"