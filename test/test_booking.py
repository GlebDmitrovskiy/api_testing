from config.base_test import BaseTest
import pytest


class TestBooking(BaseTest):
    def test_positive_create_booking(self):
        response = self.api_booking.create_booking(firstname="jim", lastname="Brown", totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        print(response.json())
        assert response.status_code == 200
