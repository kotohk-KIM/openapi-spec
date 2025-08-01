from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from datetime import datetime

app = FastAPI()

# ✅ GPT가 호출할 수 있도록 CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ GPT function call에 맞는 필드명: "text"
class TextPayload(BaseModel):
    text: str

# ✅ /evaluate 엔드포인트
@app.post("/evaluate")
async def evaluate_text(payload: TextPayload):
    return {
        "지식정합성": "91",
        "의미연결력": "88",
        "감정진정성": "85",
        "실행구조성": "92",
        "판단선택력": "89",
        "창조확산성": "87",
        "표현명료성": "93",
        "평가일시": datetime.now().isoformat()
    }

# ✅ OpenAPI 문서에 "servers" 필드 추가
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="EF 텍스트 평가 시스템",
        version="1.0.0",
        description="사용자의 텍스트(질문, 명령, 피드백 등)를 EF 기준으로 평가하는 API입니다.",
        routes=app.routes,
    )
    openapi_schema["servers"] = [
        {"url": "https://ef-question-evaluator.onrender.com"}  # ✅ Render 도메인 정확히 기입
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
