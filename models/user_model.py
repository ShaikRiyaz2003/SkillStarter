
from pydantic import BaseModel
from typing import List, Optional
class User(BaseModel):
    id: str = ''
    name: str = ''
    email: str = ''
    learning_paths: Optional[List] = []