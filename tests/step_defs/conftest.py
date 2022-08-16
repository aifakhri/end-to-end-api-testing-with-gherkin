import copy
import pytest

from endpoints.apiClient import ApiClient
from endpoints.books import BookEndpoint
from endpoints.orders import OrderEndpoint

@pytest.fixture
def apiToken():
    api = ApiClient()

    client_name = "danbo"
    client_email = "danbo@zeit.me"
    
    api.setup_api_client_detail(client_name, client_email)
    get_api_key = api.register_api_client()
    if get_api_key.status_code == 409:
        api_key = open('api_key.txt', 'r').read()
        return api_key
    else:
        api_key = get_api_key.json()["accessToken"]
        open('api_key.txt', mode='w').write(copy.deepcopy(api_key))
        return api_key

@pytest.fixture
def books():
    return BookEndpoint()

@pytest.fixture
def orders():
    return OrderEndpoint()