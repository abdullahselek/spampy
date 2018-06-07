#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from spampy import spam_classification

class SpamClassificationTests(unittest.TestCase):

    def test_load_training_set(self):
        X, y = spam_classification.load_training_set()
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)
