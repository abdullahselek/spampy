#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

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
