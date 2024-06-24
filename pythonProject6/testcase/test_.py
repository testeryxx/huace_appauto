# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：test_.py
import pytest
from config.config import FILE_PATH

from package.Execute import execute
from package.Excel import ExcelReader

sheets_name = ExcelReader(FILE_PATH).get_sheets_name()


@pytest.mark.parametrize("sheet_name", sheets_name)
def test_(sheet_name, path):
    execute(sheet_name=sheet_name, path=path)
