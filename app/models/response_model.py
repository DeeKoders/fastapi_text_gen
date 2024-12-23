
from pydantic import BaseModel

class TextGenResponse(BaseModel):
    prompt: str
    generated_text: str
