from resources.base_url import base_url

URL= base_url()

class EndPoints:
    @staticmethod
    def get_booking(id: str):
        url = URL + f"/booking/{id}"
        return url
    @staticmethod
    def post_booking():
        url = URL + "/booking"
        return url

