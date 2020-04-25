# CLI

CLI helps you to simulate **spampy** features on command line.

## Usage

First you need to install **spampy** either from PyPi or source. Then you can use sample
commands below.

```console
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
```
