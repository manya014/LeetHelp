import pickle
from sentence_transformers import SentenceTransformer
from app.config import RAG_INDEX_PATH, RAG_TOP_K
from app.utils import format_context

_model = SentenceTransformer("all-MiniLM-L6-v2")
_index = None
_docs = None


def _load_index():
    global _index, _docs
    if _index is None or _docs is None:
        with open(RAG_INDEX_PATH, "rb") as f:
            _index, _docs = pickle.load(f)


def retrieve_context(query: str) -> str:
    """
    Retrieves most relevant editorial snippets for a query.
    """
    if not query:
        return ""

    _load_index()

    query_emb = _model.encode([query])
    _, indices = _index.search(query_emb, RAG_TOP_K)

    chunks = [_docs[i] for i in indices[0]]
    return format_context(chunks)
