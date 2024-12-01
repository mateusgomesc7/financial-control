"""FastAPI app."""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """Root path."""
    return {'Hello': 'World'}
