# -*- coding : UTF-8 -*-
"""
-------------------------------------------
 @Company    : 上海米哈游天命科技有限公司
 @Project    : mihoyo-srmqatest
 @Author     : yulong.guo
 @Datetime   : 2024/11/18 20:02
 @Filename   : test_demo.py
 ------------------------------------------
"""
import logging

import pytest


class TestDemo():

    @pytest.mark.parametrize("data",[
        {"title": "1"},
        {"title": "2"},
        {"title": "3"}
    ])
    def test_supplier_page1(self, data):
        logging.info("Test title: test_supplier_page1")
