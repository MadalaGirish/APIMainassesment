import token
import requests
from requests.auth import HTTPBasicAuth

def test_auther():
    payload={

        "description": "reading book"

}
    endpoint = 'https://api-nodejs-todolist.herokuapp.com/task'
    response = requests.get(endpoint,json=payload, auth=HTTPBasicAuth('girish43@gmail.com', '90405556666'))
    Bearer = 'Bearer ' + str(token)
    headers = {
        'Authorization': Bearer}
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 401
