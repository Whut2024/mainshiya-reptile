import get_all_bank
from reptile.db_init import MainShiYaDB
from reptile.get_all_category import GetAllCategory
from reptile.get_all_full_question import GetAllFullQuestion
from reptile.get_all_question import GetAllSimpleQuestion
from reptile.http_client_init import Http2Client

database = MainShiYaDB('', 0, '', '', '')

client = Http2Client()

category = GetAllCategory(client)

bank = get_all_bank.GetAllBank(client)

simple_question = GetAllSimpleQuestion(client)

question = GetAllFullQuestion(client)

category_list = category.get_all_category()
bank_list = bank.get_all_bank(category_list)
simple_question_list = simple_question.get_all_question(bank_list)
question_list= question.get_all_full_question(simple_question_list)

# 执行SQL写入数据库