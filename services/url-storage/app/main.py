from fastapi import FastAPI, Query
import redis


app = FastAPI()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.get("/health")
def health_check():
    return {"status": "url-storage is healthy"}

@app.post("/store")
def store_url(code: str = Query(...), original_url: str = Query(...)):
    r.set(code, original_url)
    return {"message": "stored", "code": code}

@app.get("/retrieve/{code}")
def retrieve_url(code: str):
    url = r.get(code)
    if url:
        return {"url": url}
    return {"error": "not found"}

