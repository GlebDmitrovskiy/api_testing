from services.booking.payload_booking import PayLoadBooking
from services.booking.endpoints_bookinng import EndPoints
import requests


class Booking:
    def __init__(self):
        self.endpoints = EndPoints()
        self.payload_booking = PayLoadBooking()

    def create_booking(self, firstname: str, lastname: str, totalprice: int, depositpaid: bool, checkin: str,
                       checkout: str,
                       additionalneeds: str):
        response = requests.post(url=self.endpoints.post_booking(),
                                 json=self.payload_booking.create_booking(firstname=firstname, lastname=lastname,
                                                                          totalprice=totalprice,
                                                                          depositpaid=depositpaid, checkin=checkin,
                                                                          checkout=checkout,
                                                                          additionalneeds=additionalneeds))
        return response
