import pytest
from selenium import webdriver
from common.log import log
from common.sql import mysql_auto
from setting import ENV, DB


@pytest.fixture(scope='class')
def app():
    driver = webdriver.Chrome()  # 输入项目url
    log.info('打开浏览器')
    driver.get(ENV.url)
    driver.maximize_window()
    log.info('最大化窗口')
    driver.implicitly_wait(10)  # 隐式等待
    mysql_auto().execute(DB.sql_list)
    yield driver
    driver.quit()