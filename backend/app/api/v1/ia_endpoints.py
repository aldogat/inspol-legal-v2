from fastapi import APIRouter, HTTPException
from openai import OpenAI
import os

router = APIRouter()

def call_openai(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.choices[0].message.content

@router.post("/demanda")
async def generar_demanda(data: dict):
    prompt = data.get("prompt", "Genera una demanda legal")
    result = call_openai(prompt)
    return {"resultado": result}

@router.post("/contrato")
async def analizar_contrato(data: dict):
    prompt = data.get("prompt", "Analiza este contrato")
    result = call_openai(prompt)
    return {"resultado": result}

@router.post("/resumen")
async def resumen_expediente(data: dict):
    prompt = data.get("prompt", "Resume este expediente")
    result = call_openai(prompt)
    return {"resultado": result}

@router.post("/investigacion")
async def investigacion_legal(data: dict):
    prompt = data.get("prompt", "Realiza una investigación legal")
    result = call_openai(prompt)
    return {"resultado": result}
