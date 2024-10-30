import re
from time import sleep
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.log import log


@allure.step('鼠标左键点击')
def sel_click(driver, sel, timeout=20):
    try:
        element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(sel))
        element.click()
        sleep(0.2)
        chinese_data = re.sub('[^\u4e00-\u9fa5^]', '', str(sel))
        if len(chinese_data) > 0:
            log.info('点击{}'.format(chinese_data))
        return True
    except Exception as e:
        log.error('无法定位到元素,{},异常为{}'.format(sel, e))
        raise e


@allure.step('输入内容')
def sel_send_keys(diver, sel, value, timeout=10):
    try:
        WebDriverWait(diver, timeout).until(expected_conditions.element_to_be_clickable(sel)).clear()
        sleep(0.2)
        WebDriverWait(diver, timeout).until(expected_conditions.element_to_be_clickable(sel)).send_keys(value)
        sleep(0.2)
        chinese_data = re.sub('[^\u4e00-\u9fa5^]', '', str(sel))
        if len(chinese_data) > 0:
            log.info('点击{}，输入{}'.format(chinese_data, value))
        return True
    except Exception as e:
        log.error('无法定位到元素,{},异常为{}'.format(sel, e))

@allure.step('元素可见')
def element_visibility(diver, sel, timeout=30):
    try:
        WebDriverWait(diver, timeout).until(expected_conditions.element_to_be_clickable(sel))
        sleep(2)
        log.info('画面元素加载完毕')
        return True
    except Exception as e:
        log.error('加载过时仍无法发现元素,错误为{}'.format(e))
        raise e


@allure.step('获取指定元素txt值')
def get_text(diver, els, mode=0, timeout=10):
    try:
        element = WebDriverWait(diver, timeout).until(expected_conditions.presence_of_element_located(els))
        if mode == 0:
            log.info('获取数据{}'.format(element.text))
            return element.text
        elif mode == 1:
            log.info(element.get_attribute('value'))
            return element.get_attribute('value')
    except Exception as e:
        log.error('获取,错误为{}'.format(e))
        raise e
