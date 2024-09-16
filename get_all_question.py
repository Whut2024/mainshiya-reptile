import http_client_init


class GetAllSimpleQuestion:
    def __init__(self, client: http_client_init.Http2Client):
        self.client = client

    def get_all_question(self, bank_list: list):
        total_simple_question = set()

        url = 'https://api.mianshiya.com/api/question_bank/list_question'

        for single_bank in bank_list:
            json_data = {
                "questionBankId": single_bank["id"],
                "pageSize": 20,
                "current": 1
            }

            total_num = 10000
            while json_data["current"] * json_data['pageSize'] <= total_num:
                response = self.client.post_request(url=url, data=json_data)

                data = response.json()['data']
                print(data)
                simple_question_list = data['records']
                for simple_question in simple_question_list:
                    total_simple_question.add(simple_question)

                json_data['current'] += 1
                total_num = int(data['total'])

        print(total_simple_question)
        return total_simple_question



