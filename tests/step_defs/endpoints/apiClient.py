from .bases import BaseClass



class ApiClient(BaseClass):

    def __init__(self):
        super().__init__(endpoint="/api-clients/")

    def setup_api_client_detail(self, name, email):
        self._request_body["clientName"] = name
        self._request_body["clientEmail"] = email

    def register_api_client(self):
        return self._send_post_requests(apiClient=True)