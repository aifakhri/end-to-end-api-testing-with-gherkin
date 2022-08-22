import requests
import copy


## Setup API param
base_url = "https://simple-books-api.glitch.me"
endpoint = "/orders/"
endpoint_url = base_url + endpoint

apiToken = open("api_key.txt", "r").read()

header = {}
header["Authorization"] = apiToken 


## Delte all orders
copy_url = copy.deepcopy(endpoint_url)
get_all_order = requests.get(endpoint_url, headers=header)
orders = get_all_order.json()
for order in orders:
    orderId = order["id"]
    endpoint_url = endpoint_url + orderId
    print("Deleting Order Record.....")
    response = requests.delete(endpoint_url, headers=header)
    if response.status_code == 204:
        print(f"Delete is successfull, status code is {response.status_code}")
        endpoint_url = copy_url
    else:
        print(f"Delete is failed, status code is {response.status_code}")
        endpoint_url = copy_url