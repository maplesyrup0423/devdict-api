from fastapi import FastAPI, HTTPException, Query
import json
import random

app = FastAPI(title="IT 용어 사전 API", description="개발자 취준용 IT 용어 REST API", version="1.0.0")

# 데이터 로드
with open("terms.json", "r", encoding="utf-8") as f:
    terms = json.load(f)


@app.get("/terms", summary="전체 용어 목록 조회")
def get_terms(keyword: str = Query(None), category: str = Query(None)):
    results = terms

    # 키워드 검색
    if keyword:
        results = [t for t in results if keyword.lower() in t["term"].lower() or keyword.lower() in t["description"].lower()]

    # 카테고리 필터
    if category:
        results = [t for t in results if t["category"].lower() == category.lower()]

    return {"count": len(results), "results": results}


@app.get("/terms/random", summary="랜덤 용어 반환")
def get_random_term():
    return random.choice(terms)


@app.get("/terms/{term_id}", summary="특정 용어 상세 조회")
def get_term(term_id: int):
    for t in terms:
        if t["id"] == term_id:
            return t
    raise HTTPException(status_code=404, detail="해당 ID의 용어를 찾을 수 없습니다.")



