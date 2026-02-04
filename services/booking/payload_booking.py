class PayLoadBooking:

    @staticmethod
    def create_booking(firstname: str, lastname: str, totalprice: int, depositpaid: bool, checkin, checkout,
                       additionalneeds: str):
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout,
            },
            "additionalneeds": additionalneeds
        }
        return data

    @staticmethod
    def update_booking(firstname: str, lastname: str, totalprice: int, depositpaid: bool, checkin, checkout,
                       additionalneeds: str):
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout,
            },
            "additionalneeds": additionalneeds
        }
        return data

    @staticmethod
    def partial_update_booking(**kwargs):
        data = {}
        for key, value in kwargs.items():
            data[key] = value
        print(data)
        return data
