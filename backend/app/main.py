from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS CONFIGURATION (CRITICAL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
        "chrome-extension://*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Request model
# ------------------------
class SolveRequest(BaseModel):
    title: str
    description: str
    user_query: str

# ------------------------
# API route
# ------------------------
@app.post("/solve")
def solve(req: SolveRequest):
    return {
        "answer": f"Received question: {req.title}\nQuery: {req.user_query}"
    }
