from services.auth.endpoits import EndPoints
from services.auth.payload import Payload
import requests


class AuthApi:
    def __init__(self):
        self.payload = Payload
        self.endpoints = EndPoints

    def create_token(self, username: str, password: str):
        response = requests.post(
            url=self.endpoints.post_auth(),
            json=self.payload.create_token(username=username, password=password)
        )
        return response


