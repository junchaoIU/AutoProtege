# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""

class InitialOwl(object):

    def __init__(self):
        self.owl = None

    def __call__(self, domainName):
        """
            initial a new owlFile
            :param domainName: domainName of the ontology model
            """
        owl = """
        <?xml version="1.0"?>
        <rdf:RDF xmlns="http://www.owl-ontologies.com/""" + domainName + """#"
             xml:base="http://www.owl-ontologies.com/""" + domainName + """"
             xmlns:owl="http://www.w3.org/2002/07/owl#"
             xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:xml="http://www.w3.org/XML/1998/namespace"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
             xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
             xmlns:""" + domainName + """="http://www.owl-ontologies.com/""" + domainName + """#">
            <owl:Ontology rdf:about="http://www.owl-ontologies.com/""" + domainName + """"/>

            <!-- 
            ///////////////////////////////////////////////////////////////////////////////////////
            //
            // Annotation properties
            //
            ///////////////////////////////////////////////////////////////////////////////////////
             -->

             <!-- 
            ///////////////////////////////////////////////////////////////////////////////////////
            //
            // Object Properties
            //
            ///////////////////////////////////////////////////////////////////////////////////////
             -->

             <!-- 
            ///////////////////////////////////////////////////////////////////////////////////////
            //
            // Data properties
            //
            ///////////////////////////////////////////////////////////////////////////////////////
             -->

            <!-- 
            ///////////////////////////////////////////////////////////////////////////////////////
            //
            // Classes
            //
            ///////////////////////////////////////////////////////////////////////////////////////
             -->

             <!-- 
            ///////////////////////////////////////////////////////////////////////////////////////
            //
            // Individuals
            //
            ///////////////////////////////////////////////////////////////////////////////////////
             -->

        </rdf:RDF>"""
        self.owl = owl

        return self.owl
