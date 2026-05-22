import traceback, logging
from fastapi import APIRouter, HTTPException, Depends
from app.core.dependencies import get_current_user
from app.models.user import User
from openai import OpenAI
import os

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/multimodal")
async def multimodal_chat(
    data: dict,
    current_user: User = Depends(get_current_user)
):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=data.get("messages", []),
            max_tokens=1024
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        logger.error(f"Error en multimodal: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))
