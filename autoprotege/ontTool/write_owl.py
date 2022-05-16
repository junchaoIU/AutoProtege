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

class WriteOwl(object):

    def __init__(self):
        self.owl = None

    def __call__(self, owl, owlPath):
        """
        update owlFile
        """
        self.owl = owl
        f = codecs.open(owlPath, 'w', encoding='utf-8')
        f.write(owl)
        f.close()
        print("successfully updated in {}".format(owlPath))