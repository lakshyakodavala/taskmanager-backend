from pydantic import BaseModel


# Models to define request and response types

class UserRegisterRequest(BaseModel):
    email: str
    password: str


class UserLoginRequest(BaseModel):
    email: str
    password: str
