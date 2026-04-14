from typing import Optional
from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel , Field ,field_validator, EmailStr

app = FastAPI()

class UserModel(BaseModel):
    user_id: int = Field(...)
    user_name: str = Field(...,min_length=3 ,max_length= 20,example='User Name')
    user_Phone_num: int =Field(ge = 1000000000, le= 9999999999)
    user_email: EmailStr 
    user_age: Optional[int] = Field(None,gt=18, lt=60)
    user_profession: str = Field(example='developer')
    
    @field_validator('user_profession')
    def validate_profession(cls, value: str):
        allowed_roles =['developer','designer','manager']
        
        if value.lower() not in allowed_roles:
            raise ValueError(f"Profession must be one of {allowed_roles}")
        
        return value.lower()
    
@app.post('/users')
def create_user(user: UserModel):
    return user    