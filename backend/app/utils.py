def clean_text(text: str) -> str:
    """
    Normalize text before sending to LLM or embedding model.
    """
    if not text:
        return ""
    return " ".join(text.split())


def truncate_text(text: str, max_chars: int = 4000) -> str:
    """
    Prevents token explosion for LLMs.
    """
    return text[:max_chars]


def format_context(chunks: list[str]) -> str:
    """
    Formats RAG chunks nicely for prompt injection.
    """
    if not chunks:
        return "No additional context found."

    return "\n---\n".join(chunks)
