# -*- coding: utf-8 -*-
"""
    @File: keylib.py
    @Desc: 关键字库
    @Time: 2021/11/28 10:55 上午
    @Author: Wan Wenlong
"""
import time
from selenium.webdriver.common.by import By


def open(driver, target, value):
    try:
        driver.get(value)
        return True
    except Exception as e:
        return False


def input(driver, target, value):
    how, what = target.split('=', 1)
    try:
        element = driver.find_element(set_by(how), what)
        element.clear()
        element.send_keys(value)
        return True
    except Exception as e:
        return None


def click(driver, target, value):
    how, what = target.split('=', 1)
    try:
        element = driver.find_element(set_by(how), what)
        element.click()
        return True
    except Exception as e:
        return None


def sleep(timeout=1):
    time.sleep(timeout)


def wait(timeout=1):
    pass


def will_has(driver, how, what):
    try:
        driver.find_element(set_by(how), what)
    except Exception as e:
        return None
    return True


def will_in(driver, target, value):
    assert value in driver.page_source


def will_equal(driver, target: str, value: str):
    try:
        how, what = target.split('=')
        txt = driver.find_element(set_by(how), what).text
        if txt == value:
            return True
        return False
    except Exception as e:
        return False


def set_by(how):
    if how == 'id':
        return By.ID
    if how == 'name':
        return By.NAME
    if how == 'xpath':
        return By.XPATH
    if how == 'classname':
        return By.CLASS_NAME
    if how == 'linktext':
        return By.LINK_TEXT
    if how == 'partial_linktext':
        return By.PARTIAL_LINK_TEXT
    if how == 'tagname':
        return By.TAG_NAME
    if how == 'css_selector':
        return By.CSS_SELECTOR



