# 테스트 파일

이 폴더는 PII 탐지 테스트용 샘플 파일을 저장하는 곳입니다.

## 테스트 파일 예시

### test.txt
```
이름: 홍길동
전화번호: 010-1234-5678
주민등록번호: 990101-1234567
```

### test.csv
```
이름,전화번호,이메일
김철수,010-9876-5432,kim@example.com
이영희,02-1234-5678,lee@example.com
```

**주의:** 실제 개인정보는 절대 업로드하지 마세요!
```

**5. .gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# 테스트 파일 (실제 개인정보 포함 시)
test_files/*.xlsx
test_files/*.pdf
test_files/*.docx