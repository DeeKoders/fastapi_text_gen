
from pydantic import BaseModel

class TextGenRequest(BaseModel):
    prompt: str
    max_length: int = 50
