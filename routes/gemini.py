from fastapi import APIRouter, HTTPException
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

from typing import Optional

router = APIRouter()
load_dotenv()
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

@router.get("/gemini/generate")
async def get_gemini_data(technology: str,expertise:str, time_in_months: float, goal: Optional[str] = "", known_technologies: Optional[str] = ""):
    prompt = f'''
    You are an intelligent AI assistant designed to plan a structured week wise plan to learn {technology} for a {expertise} who  has a time period of {time_in_months} months to achieve a  {technology} skills aiming to {goal}. who have the idea in technologies: {known_technologies} Don not use any kind of back ticks/special characters(newline, tab-spaces, escape sequences) and text only return json formatted text below and also add any reference links 
    {{
        -+
    learning_path_name: '',
    learning_path_description: '',
    due_date: Date,
    status: 'pending',
    tasks: [
        task_name: '',
        task_deadline: Date,
        duration_period: '',
        task_description: '',
        status: 'pending',
        scorePoints: 10,
        goals: [],
        subtasks: [
            status: 'pending',
            subtask_name: '',
            subtask_deadline: Date,
            duration_period: '',
            subtask_description: '',
            subtask_goals: [],
            reference_links: [{{
                reference_name: '',
                reference_link: URL
                }}
            ],
        ]
    }}
the response should be in a format that it should be converted using json.loads() function
'''
    # TODO: add history if specified
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return json.loads(response.text)    


