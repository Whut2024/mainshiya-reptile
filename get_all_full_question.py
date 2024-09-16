import json

import http_client_init

class GetAllFullQuestion:
    def __init__(self, client:http_client_init.Http2Client):
        self.client = client

    def get_all_full_question(self, simple_question_list: list):
        url = 'https://api.mianshiya.com/api/question/get/vo?questionId='

        total_question = []

        for simple_question in simple_question_list:
            response = self.client.get_request(url=(url + str(simple_question['id'])))

            json_data = response.json()['data']
            print(json_data)

            total_question.append(json_data)

        return total_question
