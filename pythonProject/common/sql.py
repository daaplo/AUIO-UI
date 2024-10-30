import mysql.connector
import pytest
from common.log import log
from testcase.setting import DB


class mysql_auto():
    def __init__(self):
        self.conn = mysql.connector.connect(**DB.config)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql_list):
        try:
            for i in sql_list:
                self.cursor.execute(i)
            self.conn.commit()
            log.info('数据库成功还原')
            return self.cursor.fetchall()
        except Exception as e:
            log.error('执行sql错误，错误为{}'.format(e))
            raise e


if __name__ == '__main__':
    mysql_auto().execute(DB.sql_list)
