import allure
import requests

@allure.severity(allure.severity_level.MINOR)
def test_updateuser():
    payload={

        "age": 28
    }
    print(type(payload))
    Login = "https://api-nodejs-todolist.herokuapp.com/user/me"
    response =requests.put(url=Login, json=payload)
    print(response.json())