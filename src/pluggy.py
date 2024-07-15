from typing import Optional
import requests

BASE_URL = "https://api.pluggy.ai"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json"
}

class Pluggy:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_key = self.create_api_key()
    
    def _get_api_key(self):
        '''Request a new API Key to Pluggy's API''' 
        url = BASE_URL + "/auth"

        payload = {
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }

        response = requests.post(url, headers=HEADERS, json=payload)
        try:
            response.raise_for_status()
        except Exception as e:
            print(response.json())
            raise e

        api_key = response.json()['apiKey']
        return api_key

    def create_api_key(self):
        '''Validate clientId and clientSecret and return an API Key'''
        try:
            api_key = self._get_api_key()
        except Exception as e:
            raise Exception("Failed to get new api key: " + str(e))

        return api_key

    def get_item(self, item_id: str):
        '''Get an item from the API'''
        url = BASE_URL + "/items/" + item_id

        headers = HEADERS.copy()
        headers['X-API-KEY'] = self.api_key

        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(response.json())
            raise e

        item = response.json()
        return item

    def send_data_to_endpoint(self, data: dict): 
        '''Send data to the endpoint'''
        endpoint = 'https://teste-duopen.requestcatcher.com/items'
        requests.post(endpoint, json=data)
    
