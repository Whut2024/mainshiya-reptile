import time
import random
import http_client_init


class GetAllBank:
    def __init__(self, client: http_client_init.Http2Client):
        self.client = client

    def get_all_bank(self, category: list):
        total_data = set()
        url = 'https://api.mianshiya.com/api/questionBankCategory/list_questionBank'

        for single_category in category:
            json_data = {
                "pageSize": 20,
                "current": 1,
                "questionBankCategoryId": single_category['id']
            }

            total_num = 10000
            while json_data['current'] * json_data['pageSize'] < total_num:
                response = self.client.post_request(url=url, data=json_data)
                data = response.json()['data']
                print(data)

                time.sleep(1 + random.randint(1, 2))

                json_data['current'] += 1
                total_num = int(data['total'])

                bank_list = data['records']
                for single_bank in bank_list:
                    total_data.add(single_bank)

        print(total_data)
        return list(total_data)


