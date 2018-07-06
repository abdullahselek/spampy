#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spampy import (
    dataset_downloader,
    spam_classifier
)

if __name__ == '__main__':
    dataset_downloader.download_enron_dataset()
