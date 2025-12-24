import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from app.config import RAG_INDEX_PATH, RAG_DIR

# ===== SAMPLE DATA (replace later with real editorials) =====
DOCUMENTS = [
    "Two Sum is solved using a hashmap to store seen values and check complements.",
    "Binary Search works when the search space is monotonic.",
    "Sliding Window reduces time complexity for subarray problems.",
    "Prefix sums help compute range sums efficiently.",
    "DFS and BFS are graph traversal techniques with different use cases."
]

def build_index():
    print("🔧 Building RAG index...")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(DOCUMENTS)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(RAG_DIR, exist_ok=True)

    with open(RAG_INDEX_PATH, "wb") as f:
        pickle.dump((index, DOCUMENTS), f)

    print(f"✅ RAG index saved at: {RAG_INDEX_PATH}")


if __name__ == "__main__":
    build_index()
