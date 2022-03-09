# -------------------------------------------------------------------------------
# Description:  
# Reference:
# Name:   pyowl
# Author: wujunchao
# Date:   2021-12-22
# -------------------------------------------------------------------------------
import codecs
from datetime import datetime
from oneClass import *
from objectProperty import *
from dataProperty import *
from individual import *


def initialOwl(domainName):
    """
    initial a new owlFile
    :param domainName: domainName of the ontology model
    """
    f = open(str(datetime.today().date())+str(domainName)+".owl", "w+", encoding='utf-8')
    f.write("""
<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.owl-ontologies.com/"""+ domainName +"""#"
     xml:base="http://www.owl-ontologies.com/"""+ domainName +""""
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:"""+ domainName +"""="http://www.owl-ontologies.com/"""+ domainName +"""#">
    <owl:Ontology rdf:about="http://www.owl-ontologies.com/"""+ domainName +""""/>
    
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

</rdf:RDF>""")
    f.close()

def readOwl(owlPath,domainName):
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
    header = []
    opList = []
    dpList = []
    classesList = []
    indsList = []
    footer = ['</rdf:RDF>']
    f = codecs.open(owlPath, 'r', encoding='utf-8')
    lines = f.readlines()
    lines = [line.strip().replace("\n", "").replace("\r", "")for line in lines]
    for line in lines:
        """header"""
        if('<?xml version="1.0"?>' in line):
            index = lines.index(line)
            while('<owl:Ontology' not in lines[index]):
                index+=1
            header = lines[lines.index(line):index+1]
        elif('<owl:ObjectProperty' in line):
            className = line.split('#')[1].split('"')[0]
            index = lines.index(line)
            if ('/>' in line):
                oplines = [line]
            else:
                while ('</owl:ObjectProperty>' not in lines[index]):
                    index += 1
                oplines = lines[lines.index(line):index + 1]
            op = OP(domainName, className, oplines)
            opList.append(op)
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
            dpList.append(dp)
        elif ('<owl:Class' in line):
            className = line.split('#')[1].split('"')[0]
            index = lines.index(line)
            if ('/>' in line):
                Aclass = [line]
            else:
                while ('</owl:Class>' not in lines[index]):
                    index += 1
                Aclass = lines[lines.index(line):index + 1]
            oneClass = OneClass(domainName,className, Aclass)
            classesList.append(oneClass)
        elif ('<owl:NamedIndividual' in line):
            className = line.split('#')[1].split('"')[0]
            index = lines.index(line)
            if ('/>' in line):
                ind = [line]
            else:
                while ('</owl:NamedIndividual>' not in lines[index]):
                    index += 1
                indlines = lines[lines.index(line):index + 1]
            individual = Individual(domainName,className, indlines)
            indsList.append(individual)

    return header,opList,dpList,classesList,indsList,footer

def readLabel(list):
    """
    get the Individuals label from the lineList of owlFile
    :param list: the lineList in owlFile
    :return labelList: the Individuals label list
    """
    labelList = []
    for item in list:
        labelList.append(item[0].split('#')[1].split('"')[0])
    return labelList

def generateOwl(header, opList, dpList, classesList, indsList, footer, domainName):
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
    owl_write = codecs.open(str(datetime.today().date())+str(domainName)+".owl", 'w', encoding='utf-8')
    for line in header:
        owl_write.write(line)
        owl_write.write('\n')

    for op in opList:
        for line in op.owlLines:
            owl_write.write(line)
            owl_write.write('\n')

    for dp in dpList:
        for line in dp.owlLines:
            owl_write.write(line)
            owl_write.write('\n')

    for oneClass in classesList:
        for line in oneClass.owlLines:
            owl_write.write(line)
            owl_write.write('\n')

    for ind in indsList:
        for line in ind.owlLines:
            owl_write.write(line)
            owl_write.write('\n')

    for line in footer:
        owl_write.write(line)
        owl_write.write('\n')

    owl_write.close()

if __name__ == '__main__':
    domainName = "testKG"
    initialOwl(domainName)
    header, opList, dpList, classesList, indsList, footer = readOwl(r"D:\protegeAuto_tool\pyowl\2021-12-23testKG.owl", domainName)
    # generateOwl(header, opList, dpList, classesList, indsList, footer, "testKG")
    # classesList.append(OneClass(domainName, "时间", None))
    # classesList.append(OneClass(domainName, "时间点", None))
    # for i in classesList:
    #     if(i.className == "时间点"):
    #         i.addSuperClass("时间")
    classesList.append(OneClass(domainName, "人物", None))
    classesList.append(OneClass(domainName, "历史事件", None))
    classesList.append(OneClass(domainName, "共产党", None))
    classesList.append(OneClass(domainName, "国民党", None))
    for i in classesList:
        if(i.className == "共产党"):
            i.addSuperClass("人物")
        if(i.className == "国民党"):
            i.addSuperClass("人物")
    opList.append(OP(domainName, "妻子", None))
    opList.append(OP(domainName, "丈夫", None))
    for i in opList:
        if(i.className == "妻子"):
            i.addInverseOf("丈夫")
    dpList.append(DP(domainName, "别名", None))
    indsList.append(Individual(domainName,"孙中山",None))
    indsList.append(Individual(domainName,"孙文",None))
    indsList.append(Individual(domainName, "宋庆龄", None))
    dpList.append(DP(domainName,"外文名", None))
    for i in indsList:
        if(i.className == "孙中山"):
            i.addType("国民党")
            i.addComment("孙中山（1866年11月12日-1925年3月12日），名文，字载之，号日新，又号逸仙，又名帝象，化名中山樵，伟大的民族英雄、伟大的爱国主义者、中国民主革命的伟大先驱")
            i.addSameAs("孙文")
            i.addObjectProperty("妻子","宋庆龄")
            i.addDataProperty("外文名","Sun Yat-sen")
    op = OP(domainName, "配偶", None)
    op.addEquivalentop("妻子")
    opList.append(op)


    generateOwl(header, opList, dpList, classesList, indsList, footer, domainName)