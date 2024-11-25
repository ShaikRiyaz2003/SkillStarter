from fastapi import FastAPI
from routes.gemini_routes import router as gemini_router
from routes.user_routes import router as user_router
from routes.learnings_routes import router as learnings_router
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/healthcheck')
def healthcheck():
    return {"status": "ok"}
# Include the gemini router
app.include_router(gemini_router, tags=["Gemini"])
app.include_router(user_router, tags=["User"])
app.include_router(learnings_router, tags=["learnings"])
# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)