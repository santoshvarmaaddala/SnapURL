from fastapi import FastAPI, Request
import httpx
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

SHORTENER_URL = "http://shortener:8000"
REDIRECTOR_URL = "http://redirector:8000"


@app.get("/health")
def health_check():
    return {"status": "Api-Gateway is healthy"}


@app.get("/shorten")
async def forward_to_shortener(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SHORTENER_URL}/shorten", params=request.query_params)
        return JSONResponse(content=response.json(), status_code=response.status_code)

@app.get("/{code}")
async def forward_to_redirector(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{REDIRECTOR_URL}/{code}")
        if response.status_code == 307:
            return RedirectResponse(url=response.headers["location"], status_code=307)
        return JSONResponse(content=response.json(), status_code=response.status_code)