#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import unittest
from spampy import dataset_downloader


class DatasetDownloaderTests(unittest.TestCase):

    def test_download_enron_dataset(self):
        system = platform.system()
        if system == "Linux" or system == "Darwin":
            dataset_downloader.download_enron_dataset()
            self.assertTrue(os.path.exists('spampy/datasets/enron'))
