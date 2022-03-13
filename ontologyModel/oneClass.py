#!/usr/bin/python
# -*- coding: UTF-8 -*-

class OneClass:
    'OneClass的基类'

    def __init__(self, domainName, className, owlLines):
        if(owlLines is None or len(owlLines) == 1):
            # initial superClass
            owlLines = []
            owlLines.append('<owl:Class rdf:about="http://www.owl-ontologies.com/' + domainName + '#' + className + '">')
            owlLines.append('</owl:Class>')
        self.className = className
        self.domainName = domainName
        self.owlLines = owlLines

    def addSuperClass(self, superClassName):
        lines = self.owlLines
        lines.insert(1, '<rdfs:subClassOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + superClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateSuperClass(self, superClassName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:subClassOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:subClassOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + superClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteSuperClass(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:subClassOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)
