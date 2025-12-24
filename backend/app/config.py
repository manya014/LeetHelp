import os
from dotenv import load_dotenv

load_dotenv()

# ===== LLM CONFIG =====
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"

# ===== RAG CONFIG =====
RAG_TOP_K = 3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAG_DIR = os.path.join(BASE_DIR, "rag")
RAG_INDEX_PATH = os.path.join(RAG_DIR, "editorials.pkl")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in environment")
