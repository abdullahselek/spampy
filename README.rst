spampy
======

.. image:: https://github.com/abdullahselek/spampy/workflows/spampy%20ci/badge.svg
    :target: https://github.com/abdullahselek/spampy/actions

.. image:: https://img.shields.io/pypi/v/spampy.svg
    :target: https://pypi.python.org/pypi/spampy/

.. image:: https://img.shields.io/pypi/pyversions/spampy.svg
    :target: https://pypi.org/project/spampy

.. image:: https://pepy.tech/badge/spampy
    :target: https://pepy.tech/project/spampy

.. image:: https://img.shields.io/conda/vn/conda-forge/spampy?logo=conda-forge
    :target: https://anaconda.org/conda-forge/spampy

.. image:: https://anaconda.org/conda-forge/spampy/badges/latest_release_date.svg
    :target: https://anaconda.org/conda-forge/spampy

.. image:: https://anaconda.org/conda-forge/spampy/badges/license.svg
    :target: https://anaconda.org/conda-forge/spampy

Spam filtering module with Machine Learning using SVM. **spampy** is a classifier that uses ``Support Vector Machines``
which tries to classify given raw emails if they are spam or not.

Support vector machines (SVMs) are supervised learning models with associated learning algorithms that analyze data used
for classification and regression analysis. Given a set of training examples, each marked as belonging to one or the other
of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making
it a non-probabilistic binary linear classifier.

Many email services today provide spam filters that are able to classify emails into spam and non-spam email with high accuracy.
**spampy** is a learning project that you can use filtering spam mails.

**spampy** uses two different datasets for classification. One of the datasets is already imported inside the project under ``spampy/datasets/`` folder.
Second dataset is `enron-spam <http://www.aueb.gr/users/ion/data/enron-spam/>`_ dataset and inside the ``spampy`` folder I created a shell script which
downloads and extract it for you.

Project tree
------------

* email_processor ``Helper to collect features and labels from datasets.``
* spam_classifier ``Classifies given raw emails.``
* dataset_downloader ``Enron dataset downloader which uses dataset_downloader.sh``

Dependency List
---------------

* scikit_learn
* scipy
* numpy
* nltk
* click (for CLI)

Two main function of ``spam_classifier`` classifies given raw email.

* ``classify_email``
* ``classify_email_with_enron``

Installing
----------

You can install spampy using Python Package Index::

    $ pip install spampy

Install with conda from the Anaconda conda-forge channel::

    $ conda install -c conda-forge spampy

Install from its source repository on GitHub::

    $ pip install -e git+https://github.com/abdullahselek/spampy#egg=spampy

CLI
---

For available commands ``python -m spampy -h``

.. code-block::

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
