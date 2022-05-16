# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""

import codecs

class ReadOwl(object):

    def __init__(self):
        self.owl = None

    def __call__(self, owlPath):
        """
        read owlFile
        """
        f = codecs.open(owlPath, 'r', encoding='utf-8')
        return f.read()

