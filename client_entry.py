from pydantic import BaseModel

class HealthProgramInput(BaseModel):
    name: str
    desc: str