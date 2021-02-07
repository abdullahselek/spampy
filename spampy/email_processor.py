#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import nltk
import os
import numpy as np
import codecs
import multiprocessing as mp

from collections import Counter
from typing import Dict, List, Tuple


def preprocess(email: str) -> str:
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
    email = re.sub("<[^<>]+>", " ", email)
    # Any numbers get replaced with the string 'number'
    email = re.sub("[0-9]+", "number", email)
    # Any word starting with http or https:// replaced with 'httpaddr'
    email = re.sub(r"(http|https)://[^\s]*", "httpaddr", email)
    # Strings with "@" in the middle are considered emails --> 'emailaddr'
    email = re.sub(r"[^\s]+@[^\s]+", "emailaddr", email)
    # The '$' sign gets replaced with 'dollar'
    email = re.sub("[$]+", "dollar", email)
    return email


def create_tokenlist(email: str) -> List:
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
    tokens = re.split(
        r"[ \@\$\/\#\.\-\:\&\*\+\=\[\]\?\!\(\)\{\}\,\'\"\>\_\<\;\%]", email
    )
    # Loop over each word and use a stemmer to shorten it,
    tokenlist = []
    for token in tokens:
        # Remove any non alphanumeric characters
        token = re.sub("[^a-zA-Z0-9]", "", token)
        # Use the Porter stemmer to stem the word
        stemmed = stemmer.stem(token)
        # Pass empty tokens
        if not len(token):
            continue
        # Save a list of all unique stemmed words
        tokenlist.append(stemmed)
    return tokenlist


def get_vocablary_dict(
    path: str = "spampy/datasets", filename: str = "vocablary.txt"
) -> Dict:
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
    with open(os.path.join(path, filename), "r") as f:
        for line in f:
            (val, key) = line.split()
            vocablary_dict[int(val)] = key
    return vocablary_dict


def get_vocablary_indices(email: str, vocablary_dict: Dict) -> List:
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
    index_list = [
        vocablary_dict[token] for token in tokenlist if token in vocablary_dict
    ]
    return index_list


def feature_vector_from_email(email: str, vocablary_dict: Dict) -> Dict:
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
    result = np.zeros((n, 1))
    vocablary_indices = get_vocablary_indices(email, vocablary_dict)
    for index in vocablary_indices:
        result[index] = 1
    return result


def listdir(directory: str) -> List:
    """
    A specialized version of os.listdir() that ignores files that
    start with a leading period.

    Especially dismissing .DS_STORE s.
    """
    filelist = os.listdir(directory)
    return [x for x in filelist if not (x.startswith("."))]


def enron_processor(emails_dir: str, return_dict: Dict) -> Dict:
    """
    A function which processes .txt email files into lists
    and returns in a dictionary.

    Args:
      emails_dir (str):
        Root folders for emails.
      return_dict (dict):
        Shared dict for processed datas.
    """

    all_words = []
    dirs = [os.path.join(emails_dir, f) for f in listdir(emails_dir)]
    for d in dirs:
        emails = [os.path.join(d, f) for f in listdir(d)]
        for mail in emails:
            with codecs.open(mail, "r", encoding="utf-8", errors="ignore") as m:
                for line in m:
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    list_to_remove = list(dictionary.keys())
    return_dict["all_words"] = dictionary
    return_dict["list_to_remove"] = list_to_remove


def create_enron_dictionary(root_dir: str = "spampy/datasets/enron") -> Dict:
    """
    A function which create a dictionary from enron dataset.
    Uses multiple process.

    Args:
      root_dir (str):
        Root folders for enron dataset.
    """

    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    emails_dirs = [os.path.join(root_dir, f) for f in listdir(root_dir)]
    for emails_dir in emails_dirs:
        p = mp.Process(target=enron_processor, args=(emails_dir, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    dictionary = return_dict["all_words"]
    list_to_remove = return_dict["list_to_remove"]

    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    np.save("dict_enron.npy", dictionary)
    return dictionary


def features_processor(emails_dir: str, return_dict: Dict) -> Dict:
    """
    A function which processes data features into lists
    and returns in a dictionary.

    Args:
      emails_dir (str):
        Root folders for emails.
      return_dict (dict):
        Shared dict for processed datas.
    """

    features_matrix = return_dict["features_matrix"]
    train_labels = return_dict["train_labels"]
    docID = 0
    enron_dict = return_dict["enron_dict"]
    dirs = [os.path.join(emails_dir, f) for f in os.listdir(emails_dir)]
    for d in dirs:
        emails = [os.path.join(d, f) for f in os.listdir(d)]
        for mail in emails:
            with open(mail) as m:
                all_words = []
                for line in m:
                    words = line.split()
                    all_words += words
                for word in all_words:
                    wordID = 0
                    for i, d in enumerate(enron_dict):
                        if d[0] == u"word":
                            wordID = i
                            features_matrix[docID, wordID] = all_words.count(word)
            train_labels[docID] = int(mail.split(".")[-2] == "spam")
            docID = docID + 1
    return_dict["features_matrix"] = features_matrix
    return_dict["train_labels"] = train_labels


def extract_enron_features(root_dir: str = "spampy/datasets/enron") -> Tuple:
    """
    A function creates features and labels from enron dataset.
    Uses multiple process and returns in a tuple.

    Args:
      root_dir (str):
        Root folders for enron dataset.
    """

    enron_dict = create_enron_dictionary(root_dir)
    manager = mp.Manager()
    return_dict = manager.dict()
    return_dict["enron_dict"] = enron_dict
    features_matrix = np.zeros((33716, 3000))
    train_labels = np.zeros(33716)
    return_dict["features_matrix"] = features_matrix
    return_dict["train_labels"] = train_labels
    jobs = []
    emails_dirs = [os.path.join(root_dir, f) for f in os.listdir(root_dir)]
    for emails_dir in emails_dirs:
        p = mp.Process(target=features_processor, args=(emails_dir, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    features_matrix = return_dict["features_matrix"]
    train_labels = return_dict["train_labels"]
    return np.array(features_matrix), np.array(train_labels)
