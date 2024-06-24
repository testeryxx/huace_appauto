# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：execute.py
import json
import time

from package.Excel import ExcelReader

from package.Context import Context

from package import KeyWords


def execute(sheet_name, path=None):
    file_object = ExcelReader(path, sheet_name=sheet_name)
    data = file_object.get_case_data()
    for i in data:
        action = i["action"]
        action_values = i.get("action_values", [None])
        print(action_values)
        keys_func = getattr(KeyWords, action)  # 得到关键字函数
        keys_func(*action_values)
