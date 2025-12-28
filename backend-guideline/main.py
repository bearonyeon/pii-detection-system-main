from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# DB 초기화
models.Base.metadata.create_all(bind=database.engine)

def generate_guideline(findings: list) -> str:
    """발견된 개인정보 항목 중 가장 높은 점수를 기준으로 맞춤 가이드라인 생성"""
    if not findings:
        return "탐지된 개인정보가 없습니다. 안전하게 관리하시기 바랍니다."

    max_score = max([f['score'] for f in findings]) if findings else 0
    
    if max_score >= 10:
        return (
            "[심각] 고유 식별 정보 및 민감 정보(주민번호, 여권 등)가 탐지되었습니다. "
            "권장 조치: 업로드 즉시 차단, 데이터 암호화 저장, 목적 달성 시 즉시 삭제를 권고합니다."
        )
    elif max_score >= 8:
        return (
            "[위험] 금융 정보 및 생체 정보(카드, 계좌, 생체인식 등)가 탐지되었습니다. "
            "권장 조치: 업로드 차단 검토, 암호화 필수, 일정 기간 내 삭제 및 보안 관리를 권고합니다."
        )
    elif max_score >= 5:
        return (
            "[주의] 직접 식별 가능 정보(이름, 상세 주소, 휴대폰 번호)가 탐지되었습니다. "
            "권장 조치: 불필요한 항목 삭제, 데이터 마스킹 처리, 최소한의 공유 범위 설정을 권고합니다."
        )
    elif max_score >= 3:
        return (
            "[관심] 간접 식별 정보(IP, MAC 주소, 로그 등)가 탐지되었습니다. "
            "권장 조치: 데이터 보관 기간 축소, 시스템 접근 권한 최소화 및 주기적인 로그 점검을 권고합니다."
        )
    else:
        return "기타 개인정보 항목이 탐지되었습니다. 내부 보안 지침을 준수하시기 바랍니다."

@app.post("/api/save-results")
async def save_results(data: dict, db: Session = Depends(database.get_db)):
    results = data.get("results", [])
    db_items = []

    for res in results:
        guideline = generate_guideline(res.get('findings', []))
        
        db_item = models.ScanResult(
            filename=res['filename'],
            overall_score=res['overall_score'],
            risk_level=res['risk_level'],
            guideline=guideline,
            findings=res['findings']
        )
        db_items.append(db_item)
    
    if db_items:
        db.add_all(db_items)
        db.commit()

        for item in db_items:
            db.refresh(item)
        
    return {"message": "저장 완료", "count": len(db_items)}

@app.get("/api/history")
async def get_history(db: Session = Depends(database.get_db)):
    """과거 분석 이력 조회"""
    return db.query(models.ScanResult).all()