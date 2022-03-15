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

    def addComment(self, comment):
        lines = self.owlLines
        lines.insert(1, '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + comment + '</rdfs:comment>')
        self.owlLines = lines
        print(lines)

    def updateComment(self, comment):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + comment + '</rdfs:comment>')
        self.owlLines = lines
        print(lines)

    def deleteComment(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addEquivalentop(self, equivalentOPName):
        lines = self.owlLines
        lines.insert(1, '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateEquivalentop(self, equivalentOPName):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteEquivalentop(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addInverseOf(self, inverseOfOPName):
        lines = self.owlLines
        lines.insert(1, '<owl:inverseOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + inverseOfOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateInverseOf(self, inverseOfOPName):
        lines = self.owlLines
        for line in lines:
            if '<owl:inverseOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:inverseOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + inverseOfOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteInverseOf(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:inverseOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addSubPropertyOf(self, subPropertyOfOPName):
        lines = self.owlLines
        lines.insert(1, '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + subPropertyOfOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateSubPropertyOf(self, subPropertyOfOPName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + subPropertyOfOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteSubPropertyOf(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addDomain(self, domainName):
        lines = self.owlLines
        lines.insert(1, '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + domainName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateDomain(self, domainName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + domainName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteDomain(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addRange(self, rangeName):
        lines = self.owlLines
        lines.insert(1, '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + rangeName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateRange(self, rangeName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + rangeName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteRange(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:domain rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addDisjointOP(self, disjointOPName):
        lines = self.owlLines
        lines.insert(1, '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateDisjointOP(self, disjointOPName):
        lines = self.owlLines
        for line in lines:
            if '<<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointOPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteDisjointOP(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)
