from pydantic import BaseModel
from typing import Optional

class ProblemRequest(BaseModel):
    title: str
    description: str
    samples: Optional[str] = ""
    mode: str = "chat"
    user_query: Optional[str] = ""
