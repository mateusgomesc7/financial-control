"""Test the FastAPI app."""

from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)
