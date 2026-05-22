from fastapi import APIRouter, HTTPException
from openai import OpenAI
import os

router = APIRouter()

@router.post("/multimodal")
async def simple_chat(data: dict):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        messages = data.get("messages", [])
        if not messages:
            raise HTTPException(status_code=400, detail="No messages provided")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1024
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
