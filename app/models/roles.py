from enum import Enum

from pydantic import BaseModel


class RoleName(str, Enum):
    administrator = 'administrator'
    user = 'user'


class RoleBase(BaseModel):
    name: RoleName


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True
