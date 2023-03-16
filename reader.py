"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 23/02/2023
"""
import os
import sys
import json
from typing import AnyStr


class Links(object):
    def __init__(self, directory:str, file:list) -> None:
        self.LINKS = self.directory(directory=directory, file=file[0])

        self.AGENDA = self.directory(directory=directory, file=file[1])

        self.link = self.links(self.LINKS)
        self.content = self.links(self.AGENDA)

        self.GITHUB = self.link['github']
        self.KAGGLE = self.link['kaggle']
        self.HUGGING_FACE = self.link['Hugging_Face']
        self.TWITTER = self.link['twitter']
        self.OS = self.link['os']
        self.MODULE = self.link['module']
        self.API = self.link['api']

        self.AGENDA_CONTENT = self.content['agenda']
        self.CONTENT = self.content['content']
        self.MODULE_NAME = self.content['module']

        self.COOL_DOWN_TIME = 2

    def links(self, filename:str):
        with open(filename, "r") as f:
            data = json.load(f)

        return data

    def directory(self, directory:str, file:str) -> AnyStr:
        return str(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), directory, file))
