import requests
import allure
import pytest
import tests

@allure.severity(allure.severity_level.MINOR)
def test_createuser():
    payload = {

        "name": "madala girish",
        "email": "girish43@gmail.com",
        "password": "90405556666",
        "age": 23

    }
    print(type(payload))
    user = "https://api-nodejs-todolist.herokuapp.com/user/register"
    response = requests.post(url=user, json=payload)
    print(response)
    print(response.json())


