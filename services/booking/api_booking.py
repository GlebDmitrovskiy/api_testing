from services.booking.payload_booking import PayLoadBooking
from services.booking.endpoints_bookinng import EndPoints
from test.headers import Headers
import requests


class Booking:
    def __init__(self):
        self.endpoints = EndPoints()
        self.payload_booking = PayLoadBooking()
        self.headers = Headers()

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

    def get_booking(self, booking_id: str):
        response = requests.get(url=self.endpoints.get_booking(booking_id=booking_id))
        return response

    def get_bookings(self):
        response = requests.get(url=self.endpoints.get_bookings())
        return response

    def update_booking(self, booking_id: str, **data):
        response = requests.put(url=self.endpoints.update_booking(booking_id),
                                json=self.payload_booking.update_booking(**data), headers=self.headers.update_headers())

        return response

    def delete_booking(self, booking_id: str):
        response = requests.delete(url=self.endpoints.delete_booking(booking_id=booking_id),
                                   headers=self.headers.delete_headers())

        return response

    def partial_update_booking(self, booking_id: str, **data):
        response = requests.patch(url=self.endpoints.update_booking(booking_id),
                                json=self.payload_booking.partial_update_booking(**data), headers=self.headers.partial_update_headers())

        return response