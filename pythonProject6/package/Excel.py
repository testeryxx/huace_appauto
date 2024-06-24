# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：excel.py
import xlrd


class ExcelReader:

    def __init__(self, filename, sheet_name=None, sheet_index=None):
        self.workbook = xlrd.open_workbook(filename)  # 文件对象
        if not sheet_name and not sheet_index:
            self.sheet = self.workbook.sheet_by_index(0)
        elif sheet_name:
            self.sheet = self.workbook.sheet_by_name(sheet_name)
        elif sheet_index:
            self.sheet = self.workbook.sheet_by_index(sheet_index)
        self.current_row = 2  # 表示当前行号
        self.keys = []  # 初始化keys 对象

    def get_sheets_name(self):
        return self.workbook.sheet_names()

    # def get_values(self):  发现我们在第二阶段需要组织键值对的形式，有个values的命名，会冲突，所以改名
    def get_next_row(self):
        if self.current_row >= self.sheet.nrows:  # self.sheet.nrows 得到的是一个总行数
            return None
        row_data = self.sheet.row_values(self.current_row)
        self.current_row += 1
        return row_data

    def reset(self):
        self.current_row = 2

    """
    第二阶段的Excel修改，主要是为了返回的数据是键值对形式的关键字数据
    """

    def get_keys(self):
        self.keys = self.sheet.row_values(0)

    def get_case_data(self):
        self.get_keys()
        # self.keys  # 键值对的所有键

        while True:
            row = self.get_next_row()  # 键值对的所有值
            # print("row", row)
            if not row:
                break
            null_list = []  # 所有空数据的下标集合
            for i, v in enumerate(row):
                # print(i,v)  # i 是index v 是value
                if not v:
                    null_list.append(i)
            keys = []
            values = []

            for i in range(len(row)):
                if i not in null_list:
                    keys.append(self.keys[i])
                    values.append(row[i])

            # print(keys)
            # print(values)
            # 快捷方式 组合两个列表成为 dict的方式
            caps = dict(zip(keys, values))
            # print(caps)

            action, *args = caps.values()
            # print(action, args)

            """
            # 还可以简写
            if args:
                caps = {"action": action, "action_values": args}
            else:
                caps = {"action": action}

            yield caps
            """

            yield {"action": action, "action_values": args} if args else {"action": action}


if __name__ == '__main__':
    file_object = ExcelReader("/Volumes/huace/pythonProject4/工作簿1.xlsx")
    data = file_object.get_case_data()
    # file_object.get_case_data()

    # print(data.__next__())
    # print(data.__next__())
    # print(data.__next__())
    # for i in data:
    #     print(i)
