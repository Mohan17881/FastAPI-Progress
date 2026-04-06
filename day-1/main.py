from fastapi import FastAPI, HTTPException
from ModelClass import Employee
app = FastAPI()

employees = [{'emp_id':1,"emp_name":'sanjay','emp_role':'full-stack'},
             {'emp_id':2,"emp_name":'jai','emp_role':'backend'},
             {'emp_id':3,"emp_name":'sai','emp_role':'frontend'}]


@app.get('/employees')
def getAll_emp():
    return employees

@app.get('/employees/{emp_id}')
def get_emp(emp_id: int):
    for emp in employees:
        if emp['emp_id'] == emp_id:
            return emp
   
    raise HTTPException(status_code=404, detail="employee not found")
    

@app.post('/employees')
def create_user(emp: Employee):
    emp_dict = emp.dict()
    employees.append(emp_dict)
    return {"message": "Employee added successfully", "employee-data": emp_dict}

@app.put('/employees/{emp_id}')
def update_employee(emp_id: int, updated_data: Employee):
    for i in range(len(employees)):
        if employees[i]['emp_id'] == emp_id:
            updated_dict = updated_data.dict()
            updated_dict['emp_id'] = emp_id
            employees[i] = updated_dict
            return {"message":"Employee updated","employee_data":updated_dict}        
    raise HTTPException(status_code=404, detail="employee not found")

@app.delete('/employees/{emp_id}')
def delete_user(emp_id: int):
    for i in range(len(employees)):
        if employees[i]['emp_id'] == emp_id:
            delete_emp = employees.pop(i)
            return{"message": "employee deleted","employee_data": delete_emp}
    raise HTTPException(status_code=404, detail="employee not found")    