#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Individual:
    'Individual的基类'

    def __init__(self, domainName, className, owlLines):
        if(owlLines is None or len(owlLines) == 1):
            # initial Individual
            owlLines = []
            owlLines.append('<owl:NamedIndividual rdf:about="http://www.owl-ontologies.com/' + domainName + '#' + className + '">')
            owlLines.append('</owl:NamedIndividual>')
        self.className = className
        self.domainName = domainName
        self.owlLines = owlLines

    def addType(self, typeName):
        lines = self.owlLines
        lines.insert(1, '<rdf:type rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + typeName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateType(self, typeName):
        lines = self.owlLines
        for line in lines:
            if '<rdf:type rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdf:type rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + typeName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteType(self):
        lines = self.owlLines
        for line in lines:
            if '<rdf:type rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

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

    def addSameAs(self, indName):
        lines = self.owlLines
        lines.insert(1, '<owl:sameAs rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + indName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateSameAs(self, indName):
        lines = self.owlLines
        for line in lines:
            if '<owl:sameAs rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:sameAs rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + indName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteSameAs(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:sameAs rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)


    def addDataProperty(self, dpName, dpValue):
        lines = self.owlLines
        lines.insert(1, '<'+dpName+' rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + dpValue + '</'+dpName+'>')
        self.owlLines = lines
        print(lines)

    def updateDataProperty(self, dpName, dpValue):
        lines = self.owlLines
        for line in lines:
            if '<'+dpName+' rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        lines.insert(1, '<'+dpName+' rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + dpValue + '</'+dpName+'>')
        self.owlLines = lines
        print(lines)

    def deleteDataProperty(self, dpName):
        lines = self.owlLines
        for line in lines:
            if '<'+dpName+' rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addObjectProperty(self, opName, opValue):
        lines = self.owlLines
        lines.insert(1, '<'+self.domainName+':'+opName+' rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + opValue + '"/>')
        self.owlLines = lines
        print(lines)

    def updateObjectProperty(self, opName, opValue):
        lines = self.owlLines
        for line in lines:
            if '<'+self.domainName+':'+opName+' rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<'+self.domainName+':'+opName+' rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + opValue + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteObjectProperty(self, opName):
        lines = self.owlLines
        for line in lines:
            if '<'+self.domainName+':'+opName+' rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)