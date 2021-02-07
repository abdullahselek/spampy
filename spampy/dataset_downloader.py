#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def download_enron_dataset():
    """
    Downloads Enron dataset.
    """

    script_path = os.path.join("spampy", "dataset_downloader.sh")
    os.system(script_path)
