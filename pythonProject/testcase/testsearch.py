import allure
import pytest
from selenium.webdriver.common.by import By
from common.log import log
from common.sel import sel_click, sel_send_keys, get_text
from confteat import app


class TestSearch:
    @pytest.mark.parametrize('data', ['python', 'javascript'], ids=['test_search001', 'test_search002'])
    @allure.feature('搜索框处理')
    @allure.story('搜索')
    def test_search(self, data, app):  # 正向操作
        driver = app
        sel_click(driver, (By.XPATH, '//*[@id="kw"]'))
        sel_send_keys(driver, (By.XPATH, '//*[@id="kw"]'), data)
        sel_click(driver, (By.XPATH, '//*[@id="su"]'))  #搜索按钮
        log.info('测试数据:{}'.format(data))
        text = get_text(driver, (By.XPATH, '//*[@id="kw"]'), mode=1)
        if data == 'javascript':
            assert text == 'javascript'
        elif data == 'python':
            assert text == 'python'
        driver.back()

if __name__ == '__main__':
    pytest.main('-s','testsearch.py')