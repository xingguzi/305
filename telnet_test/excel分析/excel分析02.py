#!/usr/bin/env python

#-*- coding:utf-8 -*-


# file:excel分析02.py

# author:庄展兴

# datetime:2023/11/22 9:49

# software: PyCharm

'''

this is function description 

'''
# import module your need
# coding=UTF-8
import xlrd
import json


def convert2json(filename, keep_header=False):
    xlrd.Book.encoding = "utf-8"
    # 打开 Excel 文件
    workbook = xlrd.open_workbook(filename)

    # 获取第一个工作表
    worksheet = workbook.sheet_by_index(0)

    # 创建一个空列表
    data = []

    # 遍历每一行
    for row_index in range(worksheet.nrows):
        # 读取每一行的数据
        row_data = worksheet.row_values(row_index)
        # 将读取到的数据添加到列表中
        data.append(row_data)

    dic = {}
    content = []
    row = len(data)
    column = len(data[0])
    start = 1 - int(keep_header)

    for i in range(start, row, 1):
        for j in range(column):
            content.append(data[i][j])
        dic[data[i][0]] = content
        content = []

    with open('test.json', 'w', encoding='utf-8') as file:
        json.dump(dic, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    convert2json('C:\\Users\\82031\\Desktop\\test.xls', keep_header=False)