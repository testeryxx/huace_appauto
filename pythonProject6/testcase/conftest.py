# -*- coding: utf-8 -*-
# author: 华测-长风老师
# file name：conftest.py


import pytest
from config.config import FILE_PATH


@pytest.fixture
def path():
    return FILE_PATH
