import http_client_init

class GetAllCategory:
    def __init__(self, client: http_client_init.Http2Client):
        self.client = client


    def get_all_category(self):
        url = 'https://api.mianshiya.com/api/questionBankCategory/list'
        json_data = {}
        response = self.client.post_request(url=url, data=json_data)

        data = response.json()['data']
        print(data)
        return data
