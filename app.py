from fastapi import FastAPI
from routes.gemini import router as gemini_router
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Include the gemini router
app.include_router(gemini_router)

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)