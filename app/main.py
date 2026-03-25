from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}

@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}

@app.get("/version")
def version():
    logger.info("Version endpoint called")
    return {"version": "1.0.0"}