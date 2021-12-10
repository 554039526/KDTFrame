# -*- coding: utf-8 -*-
"""
    @File: database.py
    @Desc: 
    @Time: 2021/12/9 下午10:17
    @Author: Wan Wenlong
"""
import pymssql
from utils.util import getItemsSection


database_info = getItemsSection('sqlserver')


def select_respIsList(query):
    """
    调用：select(query='select list_master_id from list_listing_mster ')
    结果以 list 返回: ['222222222', '18703651000', '15981812162', '18703651002']
    :param query: 例如：
    :return:
    """
    res_list = []
    try:
        with pymssql.connect(server=database_info['host'], port=database_info['port'], database=database_info['database'],
                             user=database_info['user'], password=database_info['password']) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor:
                    res_list.append(row[0])
                return res_list
    except Exception as error:
        print(f'Database error: {error}')


def select_respIsDict(query):
    """
    调用：select(query='select list_master_id from list_listing_mster ')
    结果以 list[dict] 返回: [{'agent_mobile': '222222222'}, {'agent_mobile': '18703651000'}]
    :param query: 例如：
    :return:
    """
    try:
        with pymssql.connect(server=database_info['host'], port=database_info['port'], database=database_info['database'],
                             user=database_info['user'], password=database_info['password']) as conn:
            with conn.cursor(as_dict=True) as cursor:
                cursor.execute(query)
                res = cursor.fetchall()

                return res
    except Exception as error:
        print(f'Database error: {error}')


if __name__ == '__main__':
    res = select_respIsDict('select * from base_agent')
    print(res)

