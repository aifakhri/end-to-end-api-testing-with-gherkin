from .bases import BaseClass



class OrderEndpoint(BaseClass):
    
    _endpoint = "/orders/"

    def __init__(self):
        super().__init__(endpoint=self._endpoint)

    def setup_request_body(self, bookId, customerName):
        self._request_body["bookId"] = bookId
        self._request_body["customerName"] = customerName
        
    def setup_auth_headers(self, apiToken):
        self._auth_header["Authorization"] = apiToken

    def getting_order_id(self):
        resp = self._send_get_requests(auth=True)
        if resp.status_code == 200:
            self._orderId = resp.json()[0]["id"]
        else:
            self._orderId = open("endpoints/orderId.txt", "r").read()
        
    def submitting_book_order(self):
        return self._send_post_requests()

    def getting_all_ordered_book_records(self):
        return self._send_get_requests(auth=True)
    
    def getting_single_ordered_book_record(self, orderId=""):
        self._endpoint_url += self._orderId if (orderId == "") else orderId
        return self._send_get_requests(auth=True)
            
    def updating_ordered_book_record(self, customerName, orderId=""):
        self._customer_name["customerName"] = customerName
        self._endpoint_url += self._orderId if (orderId == "") else orderId
        return self._send_patch_requests()

    def deleting_ordered_book_record(self, orderId=""):
        self._endpoint_url += self._orderId if (orderId == "") else orderId
        return self._send_delete_requests()