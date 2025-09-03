from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: Optional[str]
    deadline: Optional[str]
    completed: bool
    list_id: Optional[int]