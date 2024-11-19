# -*- coding : UTF-8 -*-
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
