# -*- coding: utf-8 -*-
"""
    @File: util.py
    @Desc: 
    @Time: 2021/10/22 上午11:23
    @Author: Wan Wenlong
"""
# imports
import os
import datetime
import configparser
import functools
import time

# 项目根目录
root_path = os.path.dirname(os.path.dirname(__file__))

# data存放目录
data_path = os.path.join(root_path, 'data')
data_path_pc_agent = os.path.join(data_path, 'pc_agent')

# 设置report存放路径
report_path = os.path.join(root_path, 'reports')
now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
report_name = os.path.join(report_path, now + '.html')

# 设置log存放路径
log_path = os.path.join(root_path, 'logs')
log_name = os.path.join(log_path, now + '.log')

# pytest.ini的路径
file_dir = os.path.join(root_path, 'pytest.ini')

# 配置文件的路径
conf_dir = os.path.join(root_path, 'conf')
conf_path = os.path.join(conf_dir, 'conf.ini')

# 截图存放路径
if not os.path.exists(os.path.join(report_path, 'screenshots')):
    os.makedirs(os.path.join(report_path, 'screenshots'))
screenshots_path = os.path.join(report_path, 'screenshots')

cf = configparser.ConfigParser()
cf.read(conf_path)

# 图片识别用到的source image 路径
cvImage_path = os.path.join(data_path, 'cvImage')


def getItemsSection(section_name):
    options_dist = dict(cf.items(section_name))
    return options_dist


# 获取section下某一个option的值
def getOptionValue(section_name, option_name):
    value = cf.get(section_name, option_name)
    return value


def save_error_screenshot(func):
    """ 装饰方法异常时进行保存截图 """
    @functools.wraps(func)
    def wrapper(obj, *args, **kwargs):
        try:
            return func(obj, *args, **kwargs)
        except Exception as e:
            if not os.path.exists(os.path.join(screenshots_path, str(now))):
                os.makedirs(os.path.join(screenshots_path, str(now)))
            obj.driver.save_screenshot(os.path.join(os.path.join(screenshots_path, str(now)), f'{time.time()}.png'))
            raise e
    return wrapper


if __name__ == '__main__':
    res = getItemsSection('email')
    print(res)
