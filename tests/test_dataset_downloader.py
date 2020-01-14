#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from spampy import dataset_downloader


class DatasetDownloaderTests(unittest.TestCase):

    def test_download_enron_dataset(self):
        dataset_downloader.download_enron_dataset()
        self.assertTrue(os.path.exists('spampy/datasets/enron'))
