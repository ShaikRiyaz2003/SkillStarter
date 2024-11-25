from pydantic import BaseModel, Field
from typing import List, Optional
class ReferenceLink(BaseModel):
    reference_name: str
    reference_link: str

class Subtask(BaseModel):
    status: str
    subtask_name: str
    subtask_deadline: str
    duration_period: str
    subtask_description: str
    subtask_goals: List[str]
    reference_links: Optional[List[ReferenceLink]]

class Task(BaseModel):
    task_name: str
    task_deadline: str
    duration_period: str
    task_description: str
    status: str
    scorePoints: Optional[int]
    goals: List[str]
    subtasks: Optional[List[Subtask]]

class LearningPath(BaseModel):
    learning_path_name: str
    learning_path_description: str
    due_date: str
    status: str
    tasks: List[Task]
# }
