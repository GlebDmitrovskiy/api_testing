from config.base_test import BaseTest
import pytest


class TestBooking(BaseTest):
    @pytest.fixture()
    def booking_id(self):
        response = self.api_booking.create_booking(firstname="jim", lastname="Brown", totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        return response.json()["bookingid"]

    def test_positive_create_booking(self):
        response = self.api_booking.create_booking(firstname="jim", lastname="Brown", totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        print(response.json())
        assert response.status_code == 200

    def test_positive_get_booking(self, booking_id):
        response = self.api_booking.get_booking(booking_id)
        print(response.json())
        assert response.status_code == 200

    def test_positive_put_booking(self, booking_id):
        response = self.api_booking.update_booking(booking_id=booking_id,firstname="Fucking", lastname="Slave", totalprice=1488,
                                                   depositpaid=False, checkin="1488-01-01", checkout="1488-01-01",
                                                   additionalneeds="Berlin")
        print(response.json())
        assert response.status_code == 200

    def test_positive_delete_booking(self, booking_id):
        response = self.api_booking.delete_booking(booking_id=booking_id)
        assert response.status_code == 201
        assert self.api_booking.get_booking(booking_id=booking_id).status_code == 404
