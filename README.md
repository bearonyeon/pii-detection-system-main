# PII Detection System

파일 내 개인 식별 정보(PII)를 탐지하고 위험도를 점수화하여 데이터 보안 조치를 유도하는 의사 결정 대시보드

## 📌 프로젝트 개요

- **목적:** 파일 업로드 시 개인정보 자동 탐지 및 위험도 분석
- **탐지 대상:** 11종 개인정보 (주민등록번호, 여권번호, 신용카드 등)
- **지원 파일:** PDF, Excel, Word, CSV, TXT, 이미지 등

### 백엔드 실행
```bash
cd backend

# 가상환경 생성 및 활성화
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 라이브러리 설치
pip install -r requirements.txt

# 서버 실행
python app.py
```

서버가 http://localhost:5000 에서 실행됩니다.

### 프론트엔드 실행
```bash
# 새 터미널 열기
cd frontend

# 브라우저에서 index.html 파일 열기
# 또는 Live Server 사용 (VS Code 확장)
```

## 📂 프로젝트 구조
```
pii-detection-system/
├── backend/              # 백엔드 (Flask API)
│   ├── app.py           # 메인 서버 코드
│   └── requirements.txt # 필요 라이브러리
├── frontend/            # 프론트엔드 (HTML/JS)
│   └── index.html       # UI 대시보드
├── test_files/          # 테스트 파일
│   └── README.md        #테스트 파일 설명
└── README.md           # 프로젝트 설명
```

## 🔧 기술 스택

### 백엔드
- **언어:** Python 3.12
- **프레임워크:** Flask 3.0.0
- **탐지 방식:** 정규식 기반
- **라이브러리:**
  - flask-cors: CORS 처리
  - openpyxl: Excel 파일 처리
  - PyPDF2: PDF 파일 처리
  - python-docx: Word 파일 처리
  - Pillow: 이미지 메타데이터 처리

### 프론트엔드
- HTML5
- CSS3
- Vanilla JavaScript

## 📊 탐지 가능한 개인정보

| 점수 | 개인정보 유형 | 예시 |
|------|--------------|------|
| 10점 | 주민등록번호 | 990101-1234567 |
| 10점 | 여권번호 | M12345678 |
| 10점 | 운전면허번호 | 12-34-567890-12 |
| 8점 | 신용카드번호 | 4000-1234-5678-9012 |
| 8점 | 계좌번호 | 123-456789-01 |
| 5점 | 이름(한글) | 홍길동 |
| 5점 | 전화번호 | 010-1234-5678 |
| 5점 | 주소 | 서울시 강남구 테헤란로 123 |
| 3점 | IP 주소 | 192.168.0.1 |
| 3점 | MAC 주소 | 00:1A:2B:3C:4D:5E |
| 3점 | 쿠키/세션 | JSESSIONID=abc123 |

## 📖 API 문서

### POST /api/analyze
파일을 업로드하여 개인정보를 분석합니다.

**요청:**
```
Content-Type: multipart/form-data
Body: files (파일 배열)
```

**응답:**
```json
{
  "results": [
    {
      "id": 101,
      "filename": "test.xlsx",
      "scan_status": "ok",
      "overall_score": 10,
      "risk_level": "High",
      "compliance_score": 100,
      "findings": [
        {
          "id": 1,
          "type_label": "주민등록번호",
          "score": 10,
          "location": "content",
          "value_preview": "990101-1******"
        }
      ]
    }
  ]
}
```

### GET /api/health
서버 상태를 확인합니다.

**응답:**
```json
{
  "status": "healthy",
  "version": "1.0",
  "role": "Backend A - Detection Engine"
}
```


## 📝 라이선스

MIT License

## ⚠️ 주의사항

- 이 프로젝트는 교육/연구 목적으로 제작되었습니다.
- 실제 개인정보는 테스트에 사용하지 마세요.

- 실무 환경에서 사용 시 충분한 검증이 필요합니다.

