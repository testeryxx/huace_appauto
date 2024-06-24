# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：Keys.py
import json
import time
from package.Context import Context
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver import Remote


def session(url, caps):
    """启动会话"""
    d = Remote(url, json.loads(caps))
    # 使用print演示日志
    print(f"时间：[xxxx-xx-xx ss:ss:ss 启动会话]：{url}  {caps}")
    setattr(Context, "driver", d)


def find(by, value, ele_str=None):
    """寻找元素"""
    print(f"时间：[xxxx-xx-xx ss:ss:ss 寻找元素]：{by}  {value} {ele_str}")

    driver = getattr(Context, "driver")
    ele = Wait(driver, 2).until(ec.presence_of_element_located((by, value)))  # 保证元素存在
    if not ele_str:
        setattr(Context, "current_ele", ele)
    else:
        setattr(Context, ele_str, ele)


def click(ele=None):
    """元素点击"""
    print(f"时间：[xxxx-xx-xx ss:ss:ss 元素点击]：{ele}")

    if not ele:
        element = getattr(Context, "current_ele")
    else:
        element = getattr(Context, ele)
    element.click()


def send_keys(content, ele=None):
    """元素输入"""
    print(f"时间：[xxxx-xx-xx ss:ss:ss 元素输入]：{ele} {content}")

    # print("ele得到的值：", ele)
    # print("content得到的值：", content)
    if not ele:
        element = getattr(Context, "current_ele")
    else:
        element = getattr(Context, ele)

    element.send_keys(content)


def wait_ele_is_displayed(ele=None):
    """等待元素显示在界面"""
    # driver = getattr(Context,"driver") # 个人比较推荐反射机制
    if not ele:
        element = getattr(Context, "current_ele")
    else:
        element = getattr(Context, ele)
    driver = getattr(Context, "driver")
    Wait(driver, 2).until(ec.visibility_of(element))


def wait_ele_not_displayed(ele=None):
    """等待元素不显示在界面"""
    if not ele:
        element = getattr(Context, "current_ele")
    else:
        element = getattr(Context, ele)
    driver = getattr(Context, "driver")
    Wait(driver, 2).until(ec.invisibility_of_element(element))


def wait_ele_is_enabled(ele=None):
    """等待元素启用"""
    if not ele:
        element = getattr(Context, "current_ele")
    else:
        element = getattr(Context, ele)
    driver = getattr(Context, "driver")
    Wait(driver, 2).until(ec.staleness_of(element))


def sleep(secs):
    """进程休眠"""
    time.sleep(float(secs))


if __name__ == '__main__':
    from package.Excel import ExcelReader

    path = "/Volumes/huace/pythonProject4/工作簿1.xlsx"
    reader = ExcelReader(path)
    data = reader.get_next_row()
    print(data)
