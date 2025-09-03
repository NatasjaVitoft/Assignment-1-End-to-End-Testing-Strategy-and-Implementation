from dataclasses import dataclass
from typing import Optional

@dataclass
class ListTask:
    id: Optional[int]
    name: str