from .bases import BaseClass


class BookEndpoint(BaseClass):
    
    _endpoint = "/books/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)
    
    
    def getting_books(self, bookId=""):
        if bookId != "":
            self._endpoint_url += bookId
        return self._send_get_requests()