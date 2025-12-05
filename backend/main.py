from fastapi import FastAPI

app = FastAPI(title="AI English Tutor Backend")

@app.get("/")
async def root():
    return {"message": "AI Tutor Backend is running!", "status": "ok"}
