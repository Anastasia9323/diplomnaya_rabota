import requests
from config import API_SEARCH


class SearchAPI:

    def search_items(self, text, location, filters=None):
        data = {
            "text": text,
            "filters": filters or [],
            "location": location
        }

        response = requests.post(
            url=API_SEARCH,
            json=data
        )
        return response

    def search_items_invalid_method(self, text, location, filters=None):
        data = {
            "text": text,
            "filters": filters or [],
            "location": location
        }

        response = requests.put(
            url=API_SEARCH,
            json=data
        )
        return response
