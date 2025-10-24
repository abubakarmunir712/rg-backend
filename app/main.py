from fastapi import FastAPI

app = FastAPI(title="Research Genie Backend")

@app.get("/")
def root():
    return {"message": "Welcome to Research Genie API"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend running successfully"}
