from resources.base_url import base_url
URL=base_url()
class EndPoints:
    @staticmethod
    def post_auth():
        url= URL + "auth"
        return url