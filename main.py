from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/evaluate")
async def evaluate(q: Question):
    return {
        "지식정합성": "91",
        "의미연결력": "88",
        "감정진정성": "85",
        "실행구조성": "92",
        "판단선택력": "89",
        "창조확산성": "87",
        "표현명료성": "93"
    }
