from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: int
    emp_name: str
    emp_role: str