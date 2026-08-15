from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProjectStatus(str, Enum):
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    
    
def validate_deadline(value: date) -> date:
    if value < date.today():
        raise ValueError("Deadline cannot be in the past")
    return value


class ProjectCreate(BaseModel):
    project_name: str = Field(min_length=3, max_length=100)
    deadline: date
    status: ProjectStatus

    @field_validator("deadline")
    @classmethod
    def check_deadline(cls, value):
        if value < date.today():
            raise ValueError("Deadline cannot be in the past")
        return value


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    deadline: date
    status: ProjectStatus

    model_config = ConfigDict(from_attributes=True)


class TaskCreate(BaseModel):
    task_name: str = Field(min_length=3, max_length=100)
    status: TaskStatus
    project_id: int


class TaskResponse(BaseModel):
    id: int
    task_name: str
    status: TaskStatus
    project_id: int

    model_config = ConfigDict(from_attributes=True)


class ProjectWithTasks(BaseModel):
    id: int
    project_name: str
    deadline: date
    status: ProjectStatus
    tasks: list[TaskResponse]

    model_config = ConfigDict(from_attributes=True)
    

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: str
    password: str = Field(min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)
    

class UserLogin(BaseModel):
    email: str
    password: str