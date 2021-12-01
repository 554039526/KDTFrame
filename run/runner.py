# -*- coding: utf-8 -*-
"""
    @File: runner.py
    @Desc: 
    @Time: 2021/11/28 11:32 上午
    @Author: Wan Wenlong
"""
from utils.excel import *
from utils import keylib
from utils.util import *
import pytest


class TestRunner:
    data = get_data(get_sheet('case_data.xlsx'))

    @save_error_screenshot
    @pytest.mark.parametrize('test_data', data)
    def test_run(self, driver, test_data):
        self.driver = driver
        for x in test_data['step']:
            action, target, value = x.split(',', 2)
            if hasattr(keylib, action):
                f = getattr(keylib, action)
                f(driver, target, value)
            else:
                print(f'{action}不存在, 请添加')


if __name__ == '__main__':
    pytest.main(['-v', '--log-file={}'.format(log_name),
                 '--html={}'.format(report_name), '--self-contained-html', __file__])
