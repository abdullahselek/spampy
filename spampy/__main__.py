#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from spampy import __version__, dataset_downloader, spam_classifier


help_message = """
  Spam filtering module with Machine Learning using SVM.
  Usage
    $ python spampy [<options>]
  Options
    --help, -h              Display help message
    --download, -d          Download enron dataset
    --eclassify, -ec        Classify given raw email with enron dataset, prompts for raw email
    --classify, -c          Classify given raw email, prompts for raw email
    --version, -v           Display installed version
  Examples
    $ python spampy --help
    $ python spampy --download
    $ python spampy --eclassify
    $ python spampy --classify
"""

spampy_version = __version__


@click.command(add_help_option=False)
@click.option(
    "-d",
    "--download",
    is_flag=True,
    default=False,
    help="Use this command to download enron dataset",
)
@click.option(
    "-ec",
    "--eclassify",
    is_flag=True,
    default=False,
    help="Raw email string to classify, run -d (--download) before use",
)
@click.option(
    "-c", "--classify", is_flag=True, default=False, help="Raw email string to classify"
)
@click.option(
    "-v", "--version", is_flag=True, default=False, help="Display installed version"
)
@click.option("-h", "--help", is_flag=True, default=False, help="Display help message")
def main(download, eclassify, classify, version, help):
    if help:
        print(help_message)
        sys.exit(0)
    else:
        if version:
            print("koolsla" + " " + spampy_version)
        else:
            if download:
                dataset_downloader.download_enron_dataset()
            elif eclassify:
                email = click.prompt("Raw email", type=str)
                is_spam = spam_classifier.classify_email_with_enron(email)
                print(True if is_spam == 1 else False)
            elif classify:
                email = click.prompt("Raw email", type=str)
                is_spam = spam_classifier.classify_email(email)
                print(True if is_spam == 1 else False)


if __name__ == "__main__":
    main()
