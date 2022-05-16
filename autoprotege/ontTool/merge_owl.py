# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""


class MergeOwl(object):

    def __init__(self):
        self.owl = ''

    def __call__(self, class_dic):
        """
        generate a new OWLfile
        :param header: owl header
        :param opList: owl Object properties
        :param dpList: owl Data properties
        :param classesList: owl classes
        :param indsList: owl Individuals
        :param footer: owl footer
        :param domainName: owl omainName
        """

        for line in class_dic['header']:
            self.owl += line
            self.owl += '\n'

        for op in class_dic['opList']:
            for line in op.owlLines:
                self.owl += line
                self.owl += '\n'

        for dp in class_dic['dpList']:
            for line in dp.owlLines:
                self.owl += line
                self.owl += '\n'

        for oneClass in class_dic['classesList']:
            for line in oneClass.owlLines:
                self.owl += line
                self.owl += '\n'

        for ind in class_dic['indsList']:
            for line in ind.owlLines:
                self.owl += line
                self.owl += '\n'

        for line in class_dic['footer']:
            self.owl += line
            self.owl += '\n'

        return self.owl

