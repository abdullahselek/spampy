#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from spampy import (
    dataset_downloader,
    spam_classifier
)

help_message = '''
  Spam filtering module with Machine Learning using SVM.
  Usage
    $ python spampy [<options> ...]
  Options
    --help, -h              Display help message
    --download, -d          Download enron dataset
    --eclassify, -ec <str>  Classify given given raw email with enron dataset
    --classify, -c <str>    Classify given raw email
    --version, -v           Display installed version
  Examples
    $ python spampy --help
    $ python spampy --download
    $ python spampy --eclassify 'raw email'
    $ python spampy --classify 'raw email'
'''

if __name__ == '__main__':
    dataset_downloader.download_enron_dataset()
