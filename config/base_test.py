from services.auth.api_auth import AuthApi

class BaseTest:
    def setup_method(self):
        self.api_auth = AuthApi()