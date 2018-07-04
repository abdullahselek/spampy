#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import sys

def download_enron_dataset():
    script_path = os.path.join('spampy', 'dataset_downloader.sh')
    subprocess.call([script_path])
