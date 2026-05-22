from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

class Consulta(BaseModel):
    consulta: str

@router.post("/multimodal")
async def multimodal_chat(data: Consulta):
    try:

        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"user",
                    "content":data.consulta
                }
            ],
            max_tokens=1024
        )

        return {
            "reply":response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
