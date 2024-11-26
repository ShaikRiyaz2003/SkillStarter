from fastapi import APIRouter
from models.user_model import User
from models.learnings import Task, Subtask
from config.firebase_config import learning_collection, user_collection
import uuid
router = APIRouter()
@router.get("/learnings/all")
async def get_learnings(user_id: str):
    user_ref = user_collection.document(user_id)
    user = user_ref.get()
    if user.exists:
        learnings_ref = learning_collection.where('user_id', '==', user_id)
        learnings = learnings_ref.stream()
        return [learning.to_dict() for learning in learnings]
    else:
        return {"error": "User not found"}

@router.get("/learnings/{learning_id}")
async def get_learning(learning_id: str):
    learning_ref = learning_collection.document(learning_id)
    learning = learning_ref.get()
    if learning.exists:
        return learning.to_dict()
    else:
        return {"error": "Learning path not found"}

@router.post("/learnings")
async def create_learning(user_id: str, learning_data: dict):
    user_ref = user_collection.document(user_id)
    user = user_ref.get()
    if user.exists:
        new_learning_id = str(uuid.uuid4())
        new_learning_ref = learning_collection.document(new_learning_id)
        new_learning_ref.set({
            'user_id': user_id,
            **learning_data
        })
        user_ref.update({
            'learning_paths': (user_ref.get().to_dict() or {}).get('learnings', []) + [new_learning_id]
        })
        return {"message": "Learning path created", "learning_id": new_learning_id}
    else:
        return {"error": "User not found"}


@router.post("/learnings/{learning_id}/tasks")
async def add_task(learning_id: str, task_data: Task):
    learning_ref = learning_collection.document(learning_id)
    learning = learning_ref.get()
    if learning.exists:
        learning_data = learning.to_dict()
        tasks = learning_data.get('tasks', []) if learning_data else []
        tasks.append(task_data.dict())
        learning_ref.update({'tasks': tasks})
        return {"message": "Task added"}
    else:
        return {"error": "Learning path not found"}


@router.post("/learnings/{learning_id}/tasks/{task_name}/subtasks")
async def add_subtask(learning_id: str, task_name: str, subtask_data: Subtask):
    learning_ref = learning_collection.document(learning_id)
    learning = learning_ref.get()
    if learning.exists:
        learning_data = learning.to_dict()
        tasks = learning_data.get('tasks', []) if learning_data else []
        for task in tasks:
            if task['task_name'] == task_name:
                subtasks = task.get('subtasks', [])
                subtasks.append(subtask_data.dict())
                task['subtasks'] = subtasks
                learning_ref.update({'tasks': tasks})
                return {"message": "Subtask added"}
        return {"error": "Task not found"}
    else:
        return {"error": "Learning path not found"}


@router.put("/learnings/{learning_id}/update/{task_name}")
async def update_task_status(learning_id: str, task_name: str, status: str):
    learning_ref = learning_collection.document(learning_id)
    learning = learning_ref.get()
    if learning.exists:
        learning_data = learning.to_dict()
        if not learning_data:
            return {"error": "Learning data not found"}
        if 'tasks' not in learning_data:
            return {"error": "No tasks found in learning path"}
        tasks = learning_data.get('tasks', []) if learning_data else []
        for task in tasks:
            if task['task_name'] == task_name:
                task['status'] = status.lower()
                learning_ref.update({'tasks': tasks})
                return {"message": "Task status updated"}
        return {"error": "Task not found"}
    else:
        return {"error": "Learning path not found"}
    
    
@router.put("/learnings/{learning_id}/update/{task_name}/subtask/{subtask_name}")
async def update_subtask_status(learning_id: str, task_name: str, subtask_name: str, status: str):
    learning_ref = learning_collection.document(learning_id)
    learning = learning_ref.get()
    if learning.exists:
        learning_data = learning.to_dict()
        if not learning_data:
            return {"error": "Learning data not found"}
        if 'tasks' not in learning_data:
            return {"error": "No tasks found in learning path"}
        tasks = learning_data.get('tasks', []) if learning_data else []
        for task in tasks:
            if task['task_name'] == task_name:
                if 'subtasks' not in task:
                    return {"error": "No subtasks found in task"}
                subtasks = task.get('subtasks', [])
                for subtask in subtasks:
                    if subtask['subtask_name'] == subtask_name:
                        subtask['status'] = status.lower()
                        learning_ref.update({'tasks': tasks})
                        return {"message": "Subtask status updated"}
                return {"error": "Subtask not found"}
        return {"error": "Task not found"}
    else:
        return {"error": "Learning path not found"}
    
    
    
