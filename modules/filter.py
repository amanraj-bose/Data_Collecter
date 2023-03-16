"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 15/02/2023
"""
from typing import AnyStr
from .preprocessor import PreProcessor
import sys, os
from .basic import path

sys.path.append("./preprocessor.py")

class Filter(object):
    def __init__(self) -> None:
        self.preprocessor = PreProcessor(
            os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'bin', 'others'))

    def clear(self, text):
        text = str(text).lower()
        return str(self.preprocessor(self.preprocessor._digit(text=text)))

    def __call__(self, text) -> AnyStr:
        return str(self.preprocessor(text=str(text)))
