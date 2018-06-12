#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import nltk
import os
import numpy as np

def preprocess(email):
    """
    Preprocess (simplifies) raw email.
    Args:
      email (str):
        Raw e-mail
    Returns:
      Processed (simplified) email
    """

    # Make e-mail lower case
    email = email.lower()
    # Strip html tags
    email = re.sub('<[^<>]+>', ' ', email)
    # Any numbers get replaced with the string 'number'
    email = re.sub('[0-9]+', 'number', email)
    # Any word starting with http or https:// replaced with 'httpaddr'
    email = re.sub('(http|https)://[^\s]*', 'httpaddr', email)
    # Strings with "@" in the middle are considered emails --> 'emailaddr'
    email = re.sub('[^\s]+@[^\s]+', 'emailaddr', email)
    # The '$' sign gets replaced with 'dollar'
    email = re.sub('[$]+', 'dollar', email)
    return email

def create_tokenlist(email):
    """
    Tokenizes it, creates a list of tokens in the e-mail.
    Args:
      email (str):
        Raw e-mail
    Returns:
      Ordered list of tokens in the e-mail.
    """
    
    # use NLTK porter stemmer
    stemmer = nltk.stem.porter.PorterStemmer()
    email = preprocess(email)
    # Split the e-mail into single words by ' ', '@', '$', '/', ...
    tokens = re.split('[ \@\$\/\#\.\-\:\&\*\+\=\[\]\?\!\(\)\{\}\,\'\"\>\_\<\;\%]', email)
    # Loop over each word and use a stemmer to shorten it,
    tokenlist = []
    for token in tokens:
        # Remove any non alphanumeric characters
        token = re.sub('[^a-zA-Z0-9]', '', token)
        # Use the Porter stemmer to stem the word
        stemmed = stemmer.stem(token)
        # Pass empty tokens
        if not len(token): continue
        # Save a list of all unique stemmed words
        tokenlist.append(stemmed)
    return tokenlist    

def get_vocablary_dict(path='spampy/datasets', filename='vocablary.txt'):
    """
    Add vocablary text file content into a dictionary.
    Args:
      path (str):
        Vocablary file folder path.
      filename (str):
        Vocablary file name.
    Returns:
      Vocablary dict.
    """

    vocablary_dict = {}
    with open(os.path.join(path, filename), 'r') as f:
        for line in f:
            (val, key) = line.split()
            vocablary_dict[int(val)] = key
    return vocablary_dict

def get_vocablary_indices(email, vocablary_dict):
    """
    Returns a list of indices (location) of each stemmed word in email.
    Args:
      email (str):
        E-mail.
      vocablary_dict (dict):
        Vocablary dictionary created by `get_vocablary_dict`.
    Returns:
      Indices list.
    """

    tokenlist = create_tokenlist(email)
    index_list = [vocablary_dict[token] for token in tokenlist if token in vocablary_dict]
    return index_list

def feature_vector_from_email(email, vocablary_dict):
    """
    Returns a vector of shape (n,1) with a size of the vocablary_dict.
    If the vocab word with index == 1 is in the email, first element in
    this vector is 1, 0 otherwise.
    Args:
      email (str):
        E-mail.
      vocablary_dict (dict):
        Vocablary dictionary created by `get_vocablary_dict`.
    """

    n = len(vocablary_dict)
    result = np.zeros((n,1))
    vocablary_indices = get_vocablary_indices(email, vocablary_dict)
    for index in vocablary_indices:
        result[index] = 1
    return result