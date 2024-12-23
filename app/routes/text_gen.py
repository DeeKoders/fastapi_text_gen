
from fastapi import APIRouter, HTTPException
from app.models.request_model import TextGenRequest
from app.models.response_model import TextGenResponse
from app.utils.huggingface_model import generate_text

router = APIRouter()

@router.post("/generate", response_model=TextGenResponse)
async def generate(request: TextGenRequest):
    try:
        output = generate_text(prompt=request.prompt, max_length=request.max_length)
        return TextGenResponse(prompt=request.prompt, generated_text=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
