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

    def addEquivalentClass(self, equivalentClassName):
        lines = self.owlLines
        lines.insert(1, '<owl:equivalentClass rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateEquivalentClass(self, equivalentClassName):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentClass rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:equivalentClass rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteEquivalentClass(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentClass rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

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

    def addDisjointClass(self, disjointClassName):
        lines = self.owlLines
        lines.insert(1, '<owl:disjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateDisjointClass(self, disjointClassName):
        lines = self.owlLines
        for line in lines:
            if '<owl:disjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:disjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointClassName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteDisjointClass(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:disjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)
