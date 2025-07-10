from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()
url_storage_url = "http://url-storage:8000"

@app.get("/health")
def health_check():
    return {"status": "Redirector is healthy"}

@app.get("/{code}")
def redirect(code: str):
    res = requests.get(f"{url_storage_url}/retrieve/{code}")

    if res.status_code == 200:
        data = res.json()
        return RedirectResponse(url=data["url"], status_code=307)
    else:
        raise HTTPException(status_code=404, detail="short code not found")