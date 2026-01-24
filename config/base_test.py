from services.auth.api_auth import AuthApi
from services.booking.api_booking import Booking
class BaseTest:
    def setup_method(self):
        self.api_auth = AuthApi()
        self.api_booking = Booking()