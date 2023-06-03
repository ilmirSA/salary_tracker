from datetime import datetime, timedelta

import jwt
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()


class Employee:
    def __init__(self, name, salary, next_raise):
        self.name = name
        self.salary = salary
        self.next_raise = next_raise


employees = {
    'maria': Employee('Maria', 50000, datetime(2023, 6, 18)),
    'ilmir': Employee('Ilmir', 60000, datetime(2023, 7, 8)),
    'vladimir': Employee('Vladimir', 70000, datetime(2023, 6, 10))
}


class Token(BaseModel):
    access_token: str
    token_type: str


def get_token(username: str, password: str):
    if username in employees and password == 'password':

        exp_time = datetime.utcnow() + timedelta(hours=1)

        token = jwt.encode({'username': username, 'exp': exp_time}, 'secret_key', algorithm='HS256')
        return {'access_token': token, 'token_type': 'bearer', }
    else:
        raise HTTPException(status_code=401, detail='Invalid username or password')


def get_salary(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail='Token is missing')
    try:
        print(authorization)

        token = authorization.split(' ')[1]

        payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        print(payload)
        username = payload['username']

        if username in employees:
            employee = employees[username]

            return {'name': employee.name, 'salary': employee.salary, 'next_raise': employee.next_raise}
        else:
            raise HTTPException(status_code=404, detail='Employee not found')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except:
        raise HTTPException(status_code=401, detail='Invalid token')


@app.post('/login', response_model=Token)
def login(username: str, password: str):
    return get_token(username, password)


@app.get('/salary')
def salary(authorization: str = Header(None)):
    return get_salary(authorization)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
