from fastapi import FastAPI, HTTPException
from service.shortner_service import ShortnerService
from strategies.base62 import Base62Generator

app = FastAPI()

storage_service_url = "http://url-storage:8000"
generator = Base62Generator()
service = ShortnerService(generator, storage_service_url)

@app.get("/health")
def health_check():
    return {"status": "Shortner is healthy"}


@app.post("/shorten")
def shorten(url: str):
    try:
        return service.shorten_url(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))