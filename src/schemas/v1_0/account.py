from src.schemas.v1_0 import *


class Login(BaseModel):
    email: str
    password: str


class Register(BaseModel):
    email: str
    mobile: str
    firstname: str
    lastname: str
    middle_name: Optional[str] = None
    password: str
    image: Optional[str] = None
