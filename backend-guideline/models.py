# Database 모델 설정
from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from database import Base

Base = declarative_base()

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    overall_score = Column(Integer)
    risk_level = Column(String)
    guideline = Column(Text)  # 생성된 가이드라인 저장
    findings = Column(JSON)   # 탐지된 세부 항목 (리스트 형태)