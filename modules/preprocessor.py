"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 11/02/2023
"""

import pickle
import os
import re
import joblib
from .basic import path

class PreProcessor(object):
    def __init__(self, path) -> None:
        self.path = os.path.join(path, "swear.pkl")

    def _clean(self, text:str):
        text = text.lower()
        result = re.sub( r'<.*?>', r'', text )
        result = re.sub( r'\S+@\S+', r'', result )
        result = re.sub(r'http\S+', '', result)
        result = re.sub( r'[^\w\s]', r'', result )
        result = result.lower()
        patterns = re.compile(r"(.)\1{2,}")
        result = patterns.sub(r"\1\1", result)
        return result

    def _swear(self, text):
        text = str(text).lower()
        swear_bert = joblib.load(self.path)
        result = []
        for i in str(text).split():
            if i not in swear_bert:
                result.append(i)

        return " ".join(result)

    def _digit(self, text):
        return str(re.sub(r'[@]', '', re.sub(r'\d+', '', str(text).lower()))).lower()

    def __call__(self, text:str):
        clean = str(self._clean(str(text)))
        swear = str(self._swear(clean))
        return swear
