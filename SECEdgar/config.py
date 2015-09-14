# -*- coding:utf-8 -*-
__all__ = [
    'DEFAULT_DATA_PATH',
    'DEFAULT_CREDENTIALS_FILE'
]

import re
import sys
import logging
import os


DEFAULT_DATA_PATH = os.path.dirname(os.path.abspath(__file__))
