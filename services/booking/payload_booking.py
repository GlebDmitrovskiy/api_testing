class PayLoadBooking:
    @staticmethod
    def get_booking(firstname: str, lastname: str, totalprice: int, depositpaid: int, checkin: str, checkout: str,
                    additionalneeds: str):
        data = {"firstname": firstname, "lastname": lastname, "totalprice": totalprice, "depositpaid": depositpaid,
                "checkin": checkin, "checkout": checkout, "additionalneeds": additionalneeds}
        return data

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
