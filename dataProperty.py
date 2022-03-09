#!/usr/bin/python
# -*- coding: UTF-8 -*-

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