from os import getenv

import requests

from source.helpers.constants import EnvironmentVariables as env_vars
from source.helpers.constants import Urls as urls


class DvlaApi:

    def __init__(self):
        self.api_key = self._load_api_key()
        self.url = self._load_request_url()

    def _get_api_key(self):
        return self.api_key

    def _get_url(self):
        return self.url

    def _load_request_url(self):
        return urls.URL_DVLA_HISTORICAL

    def make_request(self, reg: str):
        url = f"{self.url}{reg}"
        headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            raise ConnectionError(f"Request returned invalid response: {response.status_code}")
        return response.json()

    def _make_request(self, *args, **kwargs):
        return 0

    def _load_api_key(self) -> str:
        """
        Get the API key for the DVLA API
        :param env: One of (dev, prod)
        :return: Either the dev or prod key for the API
        """
        return getenv(env_vars.ENV_MOT_HISTORY_API_KEY)


if __name__ == '__main__':
    a = DvlaApi()
    print(a.make_request("RJ08GOX"))
