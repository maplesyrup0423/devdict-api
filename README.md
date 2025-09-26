# 📖 IT 용어 사전 API (Developer Dictionary API)

## 🔹 프로젝트 개요

**IT 용어 사전 API**는 자주 사용되는 IT 용어를 검색하고 랜덤으로 확인할 수 있는 REST API입니다.

주요 기능:

- 전체 용어 조회
- 키워드 검색 (한글 + 영문, 대소문자 무시)
- 카테고리 필터링
- 상세 조회
- 랜덤 용어 반환

---

## 📂 기능 목록

| 기능           | 엔드포인트                       | 설명                                         |
| -------------- | -------------------------------- | -------------------------------------------- |
| 전체 용어 조회 | `GET /terms`                     | 모든 IT 용어 반환                            |
| 키워드 검색    | `GET /terms?keyword=<키워드>`    | 한글/영문 키워드로 검색 가능                 |
| 카테고리 필터  | `GET /terms?category=<카테고리>` | 특정 분야(backend, frontend, devops 등) 조회 |
| 상세 조회      | `GET /terms/{id}`                | 특정 ID 용어 상세 정보 반환                  |
| 랜덤 용어      | `GET /terms/random`              | 랜덤으로 한 개 용어 반환                     |

---

## 📦 데이터 구조 (`terms.json` 예시)

```json
[
  {
    "id": 1,
    "term": "API",
    "category": "backend",
    "description": "API(Application Programming Interface)는 서로 다른 소프트웨어나 시스템이 상호작용할 수 있도록 도와주는 인터페이스다. 이를 통해 외부 프로그램이 기능을 호출하거나 데이터를 주고받을 수 있다."
  },
  {
    "id": 2,
    "term": "DOM",
    "category": "frontend",
    "description": "DOM(Document Object Model)은 HTML, XML 문서를 객체로 표현한 계층 구조를 말한다. JavaScript를 통해 문서 구조, 스타일, 내용 등을 동적으로 제어할 수 있다."
  }
  //생락
]
```

# IT 용어 사전 API - 설치 및 사용 가이드

## 📌 데이터 구조

- `id`: 고유 ID
- `term`: IT 용어명
- `category`: 용어 분류 (backend, frontend, database 등)
- `description`: 상세 설명 (2~3줄)

---

## 🌐 배포 URL

[https://devdict-api.vercel.app](https://devdict-api.vercel.app)

## 🧪 API 테스트

- 전체 용어: `https://devdict-api.vercel.app/terms`
- 랜덤 용어: `https://devdict-api.vercel.app/terms/random`
- 키워드 검색: `https://devdict-api.vercel.app/terms?keyword=dom`
- 카테고리별 조회: `https://devdict-api.vercel.app/terms?category=frontend`
- 상세 조회: `https://devdict-api.vercel.app/terms/1`

## 🛠 기술 스택

- **언어**: Python
- **프레임워크**: FastAPI
- **서버 실행**: Uvicorn
- **데이터 저장**: JSON (`terms.json`)
