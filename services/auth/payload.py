class Payload:
    @staticmethod
    def create_token(username: str, password: str):
        data = {"username": username, "password": password}
        return data
