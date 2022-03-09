#!/usr/bin/python
# -*- coding: UTF-8 -*-

class OP:
    'Object property的基类'

    def __init__(self, domainName, className, owlLines):
        if(owlLines is None or len(owlLines) == 1):
            # initial OP
            owlLines = []
            owlLines.append('<owl:ObjectProperty rdf:about="http://www.owl-ontologies.com/' + domainName + '#' + className + '">')
            owlLines.append('</owl:ObjectProperty>')
        self.className = className
        self.domainName = domainName
        self.owlLines = owlLines

    def addInverseOf(self, inverseOfOPName):
        lines = self.owlLines
        lines.insert(1, '<owl:inverseOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + inverseOfOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def addEquivalentop(self, equivalentOPName):
        lines = self.owlLines
        lines.insert(1, '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentOPName + '"/>')
        self.owlLines = lines
        print(lines)