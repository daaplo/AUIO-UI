import mysql.connector
from pygments.lexers import javascript


class ENV:
    url = "https://baidu.com"


class DB:
    config = {
        'user': 'root',
        'password': '123456',
        'host': 'localhost',
        'database': 'ab',
    }
    sql_list = [
        'TRUNCATE TABLE search',
        "INSERT INTO search (id, value) VALUES ('1', 'python'),( '2', 'javascript');"
    ]


if __name__ == '__main__':
    db = DB()
