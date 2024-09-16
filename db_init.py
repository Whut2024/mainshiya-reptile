import mysql.connector


class MainShiYaDB:
    def __init__(self, host, port, database, user, password):
        self.whut_friends_db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database,
            port=port,
        )

        self.whut_friends_cursor = self.whut_friends_db.cursor()


    def modify_database(self, sql, values):
        self.whut_friends_cursor.execute(sql, values)
        self.whut_friends_db.commit()


    def modify_multiple_data(self, sql, many_tuple):
        self.whut_friends_cursor.executemany(sql, many_tuple)
        self.whut_friends_db.commit()

    def close(self):
        self.whut_friends_cursor.close()
        self.whut_friends_db.close()


