# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""

from autoprotege.ontModel.dataProperty import DP
from autoprotege.ontModel.individual import Individual
from autoprotege.ontModel.objectProperty import OP
from autoprotege.ontModel.oneClass import OneClass


class SpiltOwl(object):

    def __init__(self):
        self.header = []
        self.opList = []
        self.dpList = []
        self.classesList = []
        self.indsList = []
        self.footer = ['</rdf:RDF>']
        self.class_dic = {}

    def __call__(self, owl, domainName):
        """
                read the header,opList,dpList,classesList,indsList,footer of the given owlFile
                :param owlPath: the path of the given owlFile
                :returns header: owl header
                :returns opList: owl Object properties
                :returns dpList: owl Data properties
                :returns classesList: owl classesList
                :returns indsList: owl Individuals
                :returns footer: owl footer
                :returns domainName: owl omainName
                """

        lines = owl.split("\n")
        lines = [line.strip().replace("\n", "").replace("\r", "") for line in lines]
        for line in lines:
            """header"""
            if ('<?xml version="1.0"?>' in line):
                index = lines.index(line)
                while ('<owl:Ontology' not in lines[index]):
                    index += 1
                print(index)
                self.header = lines[lines.index(line):index + 1]
            elif ('<owl:ObjectProperty' in line):
                className = line.split('#')[1].split('"')[0]
                index = lines.index(line)
                if ('/>' in line):
                    oplines = [line]
                else:
                    while ('</owl:ObjectProperty>' not in lines[index]):
                        index += 1
                    oplines = lines[lines.index(line):index + 1]
                op = OP(domainName, className, oplines)
                self.opList.append(op)
            elif ('<owl:DatatypeProperty' in line):
                className = line.split('#')[1].split('"')[0]
                index = lines.index(line)
                if ('/>' in line):
                    dplines = [line]
                else:
                    while ('</owl:DatatypeProperty>' not in lines[index]):
                        index += 1
                    dplines = lines[lines.index(line):index + 1]
                dp = DP(domainName, className, dplines)
                self.dpList.append(dp)
            elif ('<owl:Class' in line):
                try:
                    className = line.split('#')[1].split('"')[0]
                    index = lines.index(line)
                    if ('/>' in line):
                        Aclass = [line]
                    else:
                        while ('</owl:Class>' not in lines[index]):
                            index += 1
                        Aclass = lines[lines.index(line):index + 1]
                    oneClass = OneClass(domainName, className, Aclass)
                    self.classesList.append(oneClass)
                except:
                    pass
            elif ('<owl:NamedIndividual' in line):
                className = line.split('#')[1].split('"')[0]
                index = lines.index(line)
                if ('/>' in line):
                    ind = [line]
                else:
                    while ('</owl:NamedIndividual>' not in lines[index]):
                        index += 1
                    indlines = lines[lines.index(line):index + 1]
                individual = Individual(domainName, className, indlines)
                self.indsList.append(individual)
            self.class_dic = {
                "header": self.header,
                "opList": self.opList,
                "dpList": self.dpList,
                "classesList": self.classesList,
                "indsList": self.indsList,
                "footer": self.footer}


        return self.class_dic

