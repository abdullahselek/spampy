#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from spampy import spam_classifier

class SpamClassifierTests(unittest.TestCase):

    def test_load_training_set(self):
        X, y = spam_classifier.load_training_set()
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)

    def test_load_test_set(self):
        Xtest, ytest = spam_classifier.load_test_set()
        self.assertIsNotNone(Xtest)
        self.assertIsNotNone(ytest)

    def test_classify_email(self):
        with open(os.path.join('tests/data', 'spam_sample.txt'), 'r') as f:
            prediction = spam_classifier.classify_email(f.read())
            self.assertEqual(prediction, 0)
