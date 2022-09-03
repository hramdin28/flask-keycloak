from pydantic import BaseModel


class AuthDto(BaseModel):
    client_id: str
    client_secret: str
    username: str
    password: str
    grant_type: str = 'password'
