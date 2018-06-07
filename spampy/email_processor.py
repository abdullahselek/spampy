#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import nltk
import os

def preprocess(email):
    """
    Prepess (simplifies) raw email.
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
    email = re.sub('(http|https)://[^\rs]*', 'httpaddr', email)
    # Strings with "@" in the middle are considered emails --> 'emailaddr'
    email = re.sub('[^\rs]+@[^\rs]+', 'emailaddr', email)
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
    tokens = re.split('[ \r@\r$\r/\r#\r.\r-\r:\r&\r*\r+\r=\r[\r]\r?\r!\r(\r)\r{\r}\r,\'\"\r>\r_\r<\r;\r%]', email)
    tokens = tokens[0].split()
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
            vocablary_dict[key] = int(val)
    return vocablary_dict
