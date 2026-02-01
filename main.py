from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="NotebookLM API", version="1.0.0")

class AudioGenerationRequest(BaseModel):
    sources: List[str]
    instructions: Optional[str] = "Generate an engaging audio overview"

@app.get("/")
async def root():
    return {"message": "NotebookLM API is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "NotebookLM API", "version": "1.0.0"}

@app.post("/audio/generate")
async def generate_audio(request: AudioGenerationRequest):
    # TODO: Implement NotebookLM integration after login
    return {
        "status": "pending",
        "message": "NotebookLM integration pending - need to complete login first",
        "sources": request.sources
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
