from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    inst_id: Optional[str]
    inst_username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    login: Optional[str]
    password_hash: Optional[str]
    role: str  # manager | blogger

