from services.auth.api_auth import AuthApi


class Headers:
    def __init__(self):
        self.auth = AuthApi()

    def update_headers(self):
        token = self.auth.create_token(username="admin", password="password123").json()["token"]
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}"}
        return headers

    def delete_headers(self):
        token = self.auth.create_token(username="admin", password="password123").json()["token"]
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}",
                   "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=]"}
        return headers

    def partial_update_headers(self):
        token = self.auth.create_token(username="admin", password="password123").json()["token"]
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={token}"}
        return headers
