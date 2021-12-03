# -*- coding: utf-8 -*-
"""
    @File: keylib.py
    @Desc: 关键字库
    @Time: 2021/11/28 10:55 上午
    @Author: Wan Wenlong
"""
import os
import sys
import time
import cv2 as cv
from utils.util import cvImage_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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


def left_click_xy(driver, target, value):
    # try:
    ActionChains(driver).move_by_offset(int(value[0]), int(value[1])).click().perform()
    ActionChains(driver).move_by_offset(value[0]*(-1), value[1]*(-1)).perform()
    #     return True
    # except Exception as e:
    #     return e


def right_click_xy(driver, target, value):
    try:
        ActionChains(driver).move_by_offset(value[0], value[1]).context_click().perform()
        ActionChains(driver).move_by_offset(value[0]*(-1), value[1]*(-1)).perform()
        return True
    except Exception as e:
        return False


def find_image(driver, target, value):
    """
    在当前页面上找目标图片坐在坐标，返回中心坐标 (x,y)
    目前图片需存放在 data/cvImage 目录下
    :param target:
    :param driver:
    :param value: 例：../img/test.png
    :return:
    """

    # 获取当前页面的截图
    source_path = os.path.join(cvImage_path, 'source.png')
    driver.save_screenshot(source_path)

    # 获取目标图片的存放路径
    target_path = os.path.join(cvImage_path, value)

    source_image = cv.imread(source_path)
    target_image = cv.imread(target_path)

    # 使用 TM_CCOEFF_NORMED 获取目标图片与原图片的每个点的匹配度
    result = cv.matchTemplate(source_image, target_image, cv.TM_CCOEFF_NORMED)

    # 找出匹配度最高的点和最低的点，并返回对应的坐标
    match_result = cv.minMaxLoc(result)

    if match_result[1] > 0.9:  # 匹配度大于90%，视为匹配成功
        pos_start = cv.minMaxLoc(result)[3]  # 获取匹配成功后的起始坐标

        # 计算匹配对象的中心位置坐标
        x = int(pos_start[0]) + int(target_image.shape[1])/2
        y = int(pos_start[1]) + int(target_image.shape[0])/2
        if sys.platform == 'darwin':
            return (x/2, y/2)
        else:
            return (x, y)
    else:
        return None