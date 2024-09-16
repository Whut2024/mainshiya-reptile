import json

import httpx


class Http2Client:
    def __init__(self):
        self.headers = {
            'cookie': '',
            'user-agent': '',
            'content-type': 'application/json',
            'xweb_xhr': '1',
        }

        self.client = httpx.Client(http2=True)

    def get_request(self, url):
        return self.client.get(url=url, headers=self.headers)

    def post_request(self, url, data):
        return self.client.post(url=url, json=data, headers=self.headers)
