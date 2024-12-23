
from fastapi import FastAPI
from app.routes import text_gen

app = FastAPI(title="AI Text Generation API")

app.include_router(text_gen.router)
