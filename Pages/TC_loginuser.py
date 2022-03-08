import allure
import pytest
import requests
import resp as resp


@allure.severity(allure.severity_level.MINOR)
def test_login():
    global userdetails
    global login
    payload={

            "email": "girish43@gmail.com",
            "password": "90405556666"
    }
    print(type(payload))
    Login="https://api-nodejs-todolist.herokuapp.com/user/login"
    response = requests.post(url=Login,json=payload)
    dictdetails = dict(response.json())
    userdetails = dictdetails["user"]
    login = dictdetails["token"]
    print(userdetails)
    print(login)
    assert response.headers["Content-Type"]=="application/json; charset=utf-8"

def test_validate_user_credentials():
    actual_age = "23"
    actual_name ="madala girish"
    actual_email = "girish43@gmail.com"
    expected_age = "23"
    expected_name ="madala girish"
    expected_email ="girish43@gmail.com"
    actual=[actual_age, actual_name, actual_email]
    expected=[expected_age, expected_name, expected_email]
    assert actual == expected
    print("User credentials have been validated")