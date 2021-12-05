# -*- coding: utf-8 -*-
"""
    @File: conftest.py
    @Desc: 
    @Time: 2021/11/30 10:12 下午
    @Author: Wan Wenlong
"""
import pytest
from selenium import webdriver
import time


@pytest.fixture(name='driver', params=['1'], scope='module', autouse=False)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
