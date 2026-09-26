"""FastAPI application factory: builds the app and mounts the API router."""

from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(title="Bug Reproduction & Triage Assistant")
app.include_router(api_router)
