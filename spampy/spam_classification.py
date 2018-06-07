#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.io as sio

from os.path import join, dirname

# Parent directory
parent_directory_path = dirname(__file__)

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
