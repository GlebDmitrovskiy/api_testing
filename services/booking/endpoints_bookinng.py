from resources.base_url import base_url

URL = base_url()


class EndPoints:
    @staticmethod
    def get_booking(booking_id: str):
        url = URL + f"/booking/{booking_id}"
        return url

    @staticmethod
    def get_bookings():
        url = URL + f"/booking/"
        return url

    @staticmethod
    def post_booking():
        url = URL + "/booking"
        return url

    @staticmethod
    def update_booking(booking_id: str):
        url = URL + f"/booking/{booking_id}"
        return url

    @staticmethod
    def partial_update_booking(booking_id: str):
        url = URL + f"/booking/{booking_id}"
        return url

    @staticmethod
    def delete_booking(booking_id: str):
        url = URL + f"/booking/{booking_id}"
        return url
