from pydantic import BaseModel, Extra
from typing import Optional, List


class User(BaseModel):
    _id: str
    inst_id: Optional[str]
    inst_username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    login: Optional[str]
    password_hash: Optional[str]
    role: str  # manager | blogger

    class Config:
        extra = Extra.allow


class Route(BaseModel):
    _id: Optional[str]
    name: str
    description: str
    photos: List[str]

    class Config:
        extra = Extra.allow
