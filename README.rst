spampy
======

.. image:: https://codecov.io/gh/abdullahselek/spampy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/abdullahselek/spampy

+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                Linux                                    |                                       Windows                                    |
+=========================================================================+==================================================================================+
| .. image:: https://travis-ci.org/abdullahselek/spampy.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/eto8ikrjaq8438o1?svg=true |
|     :target: https://travis-ci.org/abdullahselek/spampy                 |    :target: https://ci.appveyor.com/project/abdullahselek/spampy                 |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Spam filtering module with Machine Learning using SVM. **spampy** is a classifier that uses ``Support Vector Machines``
which tries to classify given raw emails if they are spam or not.

Support vector machines (SVMs) are supervised learning models with associated learning algorithms that analyze data used
for classification and regression analysis. Given a set of training examples, each marked as belonging to one or the other
of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making
it a non-probabilistic binary linear classifier.

Many email services today provide spam filters that are able to classify emails into spam and non-spam email with high accuracy.
**spampy** is a learning project that you can use filtering spam mails.

**spampy** uses two different datasets for classification. One of the datasets is already import inside the project under ``spampy/datasets/`` folder.
Second dataset is **enron-spam** dataset and inside the ``spampy`` folder I created a shell script which downloads and extract it for you.
