from faker import Faker
from config.base_test import BaseTest
import pytest
fake=Faker()

class TestBooking(BaseTest):
    @pytest.fixture()
    def create_and_delete_booking(self):
        response = self.api_booking.create_booking(firstname=fake.first_name(), lastname=fake.last_name(), totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        booking_id=response.json()['bookingid']
        yield booking_id
        self.api_booking.delete_booking(booking_id=booking_id)



    def test_positive_create_booking(self):
        response = self.api_booking.create_booking(firstname=fake.first_name(), lastname=fake.last_name(), totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        print(response.json())
        assert response.status_code == 200

    def test_positive_get_bookings(self):
        response = self.api_booking.get_bookings()
        assert response.status_code == 200

    def test_positive_get_booking(self, create_and_delete_booking):
        response = self.api_booking.get_booking(create_and_delete_booking)
        print(response.json())
        assert response.status_code == 200

    def test_positive_put_booking(self, create_and_delete_booking):
        print(create_and_delete_booking)
        response = self.api_booking.update_booking(booking_id=create_and_delete_booking, firstname=fake.first_name(), lastname=fake.last_name(),
                                                   totalprice=1488,
                                                   depositpaid=False, checkin="1488-01-01", checkout="1488-01-01",
                                                   additionalneeds="Berlin")
        print(response.json())
        assert response.status_code == 200

    def test_positive_partial_put_booking(self, create_and_delete_booking):
        response = self.api_booking.partial_update_booking(booking_id=create_and_delete_booking, firstname=fake.first_name(), lastname=fake.last_name())
        print(response.json())
        assert response.status_code == 200

    def test_positive_delete_booking(self):
        create = self.api_booking.create_booking(firstname=fake.first_name(), lastname=fake.last_name(), totalprice=111, depositpaid=True,
                                                   checkin="2018-01-01", checkout="2019-01-01",
                                                   additionalneeds="Breakfast")
        booking_id = create.json()['bookingid']
        response = self.api_booking.delete_booking(booking_id=booking_id)
        assert response.status_code == 201
        get_response=self.api_booking.get_booking(booking_id=booking_id)
        assert get_response.status_code == 404
