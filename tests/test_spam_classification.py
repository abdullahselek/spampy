#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from spampy import spam_classification

class SpamClassificationTests(unittest.TestCase):

    def test_load_training_set(self):
        X, y = spam_classification.load_training_set()
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)

    def test_load_test_set(self):
        Xtest, ytest = spam_classification.load_test_set()
        self.assertIsNotNone(Xtest)
        self.assertIsNotNone(ytest)

    def test_predict_email(self):
        with open(os.path.join('tests/data', 'spam_sample.txt'), 'r') as f:
            prediction = spam_classification.predict_email(f.read())
            self.assertEqual(prediction, 'Spam possibility = 68.08%')
