#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import scipy.io as sio
import numpy as np

from os.path import join, dirname
from typing import List, Tuple

from sklearn import svm
from spampy import email_processor
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

# Parent directory
parent_directory_path = dirname(__file__)
# Support Vector Machine
linear_svm = svm.SVC(C=0.1, kernel="linear")
linear_svc = LinearSVC()


def load_training_set() -> Tuple[List, List]:
    """
    Load training set and return features and labels.
    Returns:
      Training features and labels.
    """

    # Training set
    training_set = join(parent_directory_path, "datasets/spamTrain.mat")
    dataset = sio.loadmat(training_set)
    X, y = dataset["X"], dataset["y"]
    return X, y


def load_test_set() -> Tuple[List, List]:
    """
    Load test set and return features and labels.
    Returns:
      Test features and labels.
    """

    training_set = join(parent_directory_path, "datasets/spamTest.mat")
    dataset = sio.loadmat(training_set)
    Xtest, ytest = dataset["Xtest"], dataset["ytest"]
    return Xtest, ytest


def train_svm():
    """
    Fit SVM with features and labels.
    """

    X, y = load_training_set()
    linear_svm.fit(X, y.flatten())


def classify_email(email: str) -> int:
    """
    Classify spam possibility of given email.
    Args:
      email (str):
        Raw e-mail.
    Returns:
      Spam or not.
    """

    train_svm()
    vocablary_dict = email_processor.get_vocablary_dict()
    feature_vector = email_processor.feature_vector_from_email(email, vocablary_dict)
    double_dimesion_email = np.reshape(feature_vector, (-1, 1899))
    spam_prediction = linear_svm.predict(double_dimesion_email)
    return spam_prediction


def classify_email_with_enron(email: str) -> int:
    """
    Classify spam possibility of given email with enron dataset.
    Args:
      email (str):
        Raw e-mail.
    Returns:
      Spam or not.
    """

    vocablary_dict = email_processor.create_enron_dictionary()
    feature_vector = email_processor.feature_vector_from_email(email, vocablary_dict)
    double_dimesion_email = np.reshape(feature_vector, (-1, 3000))
    if (
        os.path.exists("enron_features_matrix.npy")
        == False & os.path.exists("enron_labels.npy")
        == False
    ):
        features_matrix, labels = email_processor.extract_enron_features()
        np.save("enron_features_matrix.npy", features_matrix)
        np.save("enron_labels.npy", labels)
    else:
        features_matrix = np.load("enron_features_matrix.npy")
        labels = np.load("enron_labels.npy")
    X_train, _, y_train, _ = train_test_split(features_matrix, labels, test_size=0.40)
    linear_svc.fit(X_train, y_train)
    return linear_svc.predict(double_dimesion_email)
