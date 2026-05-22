from fastapi import APIRouter, HTTPException
from openai import OpenAI
import os

router = APIRouter()

@router.post("/mensaje")
async def simple_message(data: dict):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        message = data.get("message", "")
        if not message:
            raise HTTPException(status_code=400, detail="No message provided")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
            max_tokens=1024
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
