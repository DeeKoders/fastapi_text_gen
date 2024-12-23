
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt: str, max_length: int = 50) -> str:
    results = generator(prompt, max_length=max_length, num_return_sequences=1)
    return results[0]["generated_text"]
