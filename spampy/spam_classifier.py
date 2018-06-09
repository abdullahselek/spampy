#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.io as sio
import numpy as np

from os.path import join, dirname
from sklearn import svm
from spampy import email_processor

# Parent directory
parent_directory_path = dirname(__file__)
# Support Vector Machine
linear_svm = svm.SVC(C=0.1, kernel='linear')

def load_training_set():
    """
    Load training set and return features and labels.
    Returns:
      Training features and labels.
    """

    # Training set
    training_set = join(parent_directory_path, 'datasets/spamTrain.mat')
    dataset = sio.loadmat(training_set)
    X, y = dataset['X'], dataset['y']
    return X, y

def load_test_set():
    """
    Load test set and return features and labels.
    Returns:
      Test features and labels.
    """

    training_set = join(parent_directory_path, 'datasets/spamTest.mat')
    dataset = sio.loadmat(training_set)
    Xtest, ytest = dataset['Xtest'], dataset['ytest']
    return Xtest, ytest

def train_svm():
    """
    Fit SVM with features and labels.
    """

    X, y = load_training_set()
    linear_svm.fit(X, y.flatten())

def classify_email(email):
    """
    Classify spam possibility of given email.
    Args:
      email (str):
        Raw e-mail.
    Returns:
      Spam or not.
    """

    train_svm()
    processed_email = email_processor.preprocess(email)
    print(processed_email)
    vocablary_dict = email_processor.get_vocablary_dict()
    feature_vector = email_processor.feature_vector_from_email(processed_email, vocablary_dict)
    double_dimesion_email = np.reshape(feature_vector, (-1, 1899))
    spam_prediction = linear_svm.predict(double_dimesion_email)
    print(spam_prediction)
    return spam_prediction
