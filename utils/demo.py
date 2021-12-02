# -*- coding: utf-8 -*-
"""
    @File: demo.py
    @Desc: 
    @Time: 2021/12/1 9:43 下午
    @Author: Wan Wenlong
"""
from PIL import ImageGrab
import cv2 as cv
from utils.util import cvImage_path
import os


def find_image(driver, target):

    # 获取当前页面的截图
    driver.save_screenshot(os.path.join(cvImage_path, 'source.png'))
    source_path = os.path.join(cvImage_path, 'source.png')
    # ImageGrab.grab().save(source_path)

    # 获取目标图片的存放路径
    target_path = os.path.join(cvImage_path, target)

    source_image = cv.imread(source_path)
    target_image = cv.imread(target_path)

    result = cv.matchTemplate(source_image, target_image, cv.TM_CCOEFF_NORMED)

    match_result = cv.minMaxLoc(result)

    if match_result[1] > 0.9:  # 匹配度大于90%，视为匹配成功
        pos_start = cv.minMaxLoc(result)[3]  # 获取匹配成功后的起始坐标

        # 计算匹配对象的中心位置坐标
        x = int(pos_start[0]) + int(target_image.shape[1])/2
        y = int(pos_start[1]) + int(target_image.shape[0])/2
        return (x, y)
    else:
        return None


if __name__ == '__main__':
    from selenium import webdriver
    from utils.keylib import *
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://relsagent.joyi.cn/agent/home/ag/login/page')
    login = find_image(driver, 'login.png')
    print(login)
    left_click_xy(driver, None, login)





