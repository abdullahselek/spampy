#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from spampy import email_processor

class EmailProcessor(unittest.TestCase):

    def test_preprocess(self):
        processed_email = email_processor.preprocess('<xyz@hotmail.com> Do You Want To Make $1000 Or More Per Week? https://github.com')
        self.assertEqual(processed_email, '  do you want to make dollarnumber or more per week? httpaddr')

    def test_create_tokenlist(self):
        processed_email = email_processor.preprocess('<xyz@hotmail.com> Do You Want To Make $1000 Or More Per Week? https://github.com')
        tokens = email_processor.create_tokenlist(processed_email)
        self.assertEqual(len(tokens), 11)
