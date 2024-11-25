from fastapi import APIRouter, HTTPException
import os
import google.generativeai as genai
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
history = []
@router.get("/gemini/sayHello")
async def get_gemini_data(prompt: str, consider_history: bool = False):
    global history

    # Prepare chat with history if needed
    if consider_history and history:
        chat = model.start_chat(history=history)
        response = chat.send_message(prompt)
    else:
        chat = model.start_chat()
        response = chat.send_message(prompt)

    # Update history if consider_history is enabled
    if consider_history:
        history.append({'role': 'user', 'parts': prompt})
        history.append({'role': 'model', 'parts': response.text})

    return {"message": response.text, "history": history}
@router.post("/gemini")
async def create_gemini_data(data: dict):
    # Logic to create Gemini data
    return {"message": "Gemini data created", "data": data}

@router.put("/gemini/{gemini_id}")
async def update_gemini_data(gemini_id: int, data: dict):
    # Logic to update Gemini data
    if gemini_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid Gemini ID")
    return {"message": "Gemini data updated", "gemini_id": gemini_id, "data": data}

@router.delete("/gemini/{gemini_id}")
async def delete_gemini_data(gemini_id: int):
    # Logic to delete Gemini data
    if gemini_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid Gemini ID")
    return {"message": "Gemini data deleted", "gemini_id": gemini_id}