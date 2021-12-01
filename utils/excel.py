# -*- coding: utf-8 -*-
"""
    @File: excel.py
    @Desc: 
    @Time: 2021/11/28 10:48 上午
    @Author: Wan Wenlong
"""
import xlrd
from utils.util import data_path
import os


def get_sheet(file):
    file_path = os.path.join(data_path, file)
    try:
        r = xlrd.open_workbook(file_path)
        sheet = r.sheets()[0]
        return sheet
    except Exception as e:
        print(f'文件{file}打开异常！请检查文件是否存在', e)
        return None


def get_data(sheet):
    cases_info = []
    for x in range(1, sheet.nrows):
        case_info = {}
        step = sheet.row_values(x)[4].split('\n')
        case_info['step'] = step
        case_info['name'] = sheet.row_values(x)[1]
        case_info['exe'] = sheet.row_values(x)[2]
        if case_info['exe'] not in ('Y', 'y'):
            continue
        cases_info.append(case_info)

    return cases_info


if __name__ == '__main__':
    sheet = get_sheet('case_data.xlsx')
    print(get_data(sheet))

