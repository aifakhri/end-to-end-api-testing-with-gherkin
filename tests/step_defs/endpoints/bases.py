import requests
import copy




class BaseClass():

    _BASE_URL = "https://simple-books-api.glitch.me"
    
    def __init__(self, endpoint):
        self._endpoint_url = self._BASE_URL + endpoint
        self._endpoint_url_copy = copy.deepcopy(self._endpoint_url)
        self._response = object()
        self._auth_header = {}
        self._request_body = {}
        self._customer_name = {}
        self._orderId = ""
        self._error_msg = ""
        

    def _send_get_requests(self, auth=False):
        if auth == False:
            self._response = requests.get(self._endpoint_url)
            return self._response
        else:
            self._response = requests.get(self._endpoint_url, headers=self._auth_header)
            self._refreshing_endpoint_url()
            return self._response

    def _send_post_requests(self, apiClient=False):
        if apiClient == False:
            self._response = requests.post(
                url=self._endpoint_url,
                json=self._request_body,
                headers=self._auth_header
            )
            try:
                self._orderId = self._response.json()["orderId"]
            except KeyError:
                self._error_msg = self._response.json()["error"]
            return self._response
        else:
            self._response = requests.post(
                url=self._endpoint_url,
                json=self._request_body
            ) 
            return self._response

    def _send_patch_requests(self):
        self._response = requests.patch(
            url=self._endpoint_url,
            json=self._customer_name,
            headers=self._auth_header
        )
        self._refreshing_endpoint_url()
        return self._response

    def _send_delete_requests(self):
        self._response = requests.delete(
            url=self._endpoint_url,
            headers=self._auth_header
        )
        self._refreshing_endpoint_url()
        return self._response

    def _refreshing_endpoint_url(self):
        self._endpoint_url = self._endpoint_url_copy
        
    def checking_status_code(self):
        return self._response.status_code