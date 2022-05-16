# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""

class DP:
    'Data property的基类'

    def __init__(self, domainName, className, owlLines):
        if(owlLines is None or len(owlLines) == 1):
            # initial DP
            owlLines = []
            owlLines.append('<owl:DatatypeProperty rdf:about="http://www.owl-ontologies.com/' + domainName + '#' + className + '">')
            owlLines.append('</owl:DatatypeProperty>')
        self.className = className
        self.domainName = domainName
        self.owlLines = owlLines

    def addComment(self, comment):
        lines = self.owlLines
        lines.insert(1,
                     '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + comment + '</rdfs:comment>')
        self.owlLines = lines
        print(lines)

    def updateComment(self, comment):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        lines.insert(1,
                     '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' + comment + '</rdfs:comment>')
        self.owlLines = lines
        print(lines)

    def deleteComment(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addEquivalentdp(self, equivalentDPName):
        lines = self.owlLines
        lines.insert(1, '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentDPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateEquivalentdp(self, equivalentDPName):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + equivalentDPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteEquivalentdp(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:equivalentProperty rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addSubPropertyOf(self, subPropertyOfDPName):
        lines = self.owlLines
        lines.insert(1, '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + subPropertyOfDPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateSubPropertyOf(self, subPropertyOfDPName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:subPropertyOf rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + subPropertyOfDPName + '"/>')
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
        lines.insert(1, '<rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#' + rangeName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateRange(self, rangeName):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#' in line:
                lines.remove(line)
        lines.insert(1, '<rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#' + rangeName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteRange(self):
        lines = self.owlLines
        for line in lines:
            if '<rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)

    def addDisjointOP(self, disjointDPName):
        lines = self.owlLines
        lines.insert(1, '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointDPName + '"/>')
        self.owlLines = lines
        print(lines)

    def updateDisjointOP(self, disjointDPName):
        lines = self.owlLines
        for line in lines:
            if '<<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        lines.insert(1, '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' + self.domainName + '#' + disjointDPName + '"/>')
        self.owlLines = lines
        print(lines)

    def deleteDisjointOP(self):
        lines = self.owlLines
        for line in lines:
            if '<owl:propertyDisjointWith rdf:resource="http://www.owl-ontologies.com/' in line:
                lines.remove(line)
        self.owlLines = lines
        print(lines)