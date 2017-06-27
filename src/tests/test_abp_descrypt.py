#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-06-27 10:58:28

import unittest
from package.abp_decrypt import decodePHYpayload


class Test_abp_descrypt(unittest.TestCase):

    def test_getdata(self):
        payload = b'40785634128003000a6f30008fab3f'
        key = b'2b7e151628aed2a6abf7158809cf4f3c'

        descrypt = decodePHYpayload(payload, key)
        assert descrypt.getdata() == '1111'
