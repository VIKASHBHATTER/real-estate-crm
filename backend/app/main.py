from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.config import settings
from app.database import engine, Base

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Signature Realty CRM API",
    description="Enterprise Real Estate CRM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Signature Realty CRM API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
