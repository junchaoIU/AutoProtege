# -------------------------------------------------------------------------------
# Description:  
# Reference:  正式Api文件
# Name:   owl_Api
# Author: wujunchao
# Date:   2021/6/11
# -------------------------------------------------------------------------------
import codecs
import copy
import re
import os

class Parse_Owl:

    def standard_dic(self,dic):
        """字典清洗
        @param dic: 待清洗数据字典 dic
        @return: 清洗后数据字典 dic
        """
        dic_s = {}
        for key in dic.keys():
            for item in dic[key]:
                item = item.strip().replace(' ', '').replace('\r', '').replace("\n", "")
                if("<" not in item):
                    pass
                else:
                    if (key in dic_s.keys()):
                        dic_s[key].append(item)
                    else:
                        dic_s.update({key: [item]})
        return dic_s


    def get_individuals_dic(self, path):
        """获得所有实体块字典dic
        @param path: owl文件路径
        @return: 实体块字典dic, owl文件读写起点ind_start, owl文件读写起点ind_end
        """
        f = codecs.open(path, 'r', encoding='utf-8')
        pattern = re.compile(r'    <owl:NamedIndividual rdf:about="(.*#)(.*)">')
        pattern_2 = re.compile(r'    <rdf:Description rdf:about="(.*#)(.*)">')
        byt = f.readlines()
        n, ind_start, ind_end = 0,0,0
        dic = {}
        for connent in byt:
            connent = str(connent)
            match = pattern.match(connent)
            match_2 = pattern_2.match(connent)
            if match:
                s = ''
                rear = n
                while '    </owl:NamedIndividual>' not in byt[rear]:
                    rear += 1
                dic[match.group(2)] = byt[n - 5:rear + 1]
            elif match_2:
                s = ''
                rear = n
                while '    </rdf:Description>' not in byt[rear] :
                    rear += 1
                dic[match_2.group(2)] = byt[n - 5:rear + 1]
            n += 1
            if '    // Individuals' in connent:
                ind_start = n + 4
            if '</rdf:RDF>' in connent:
                ind_end = n - 1
        return dic, ind_start, ind_end


    def get_individuals_ins(self, path):
        """ owl实体类信息查询
        @param path: owl文件路径 String
        @return: list_Object: 关系 List
        @return: list_Datatype: 属性 List
        @return: list_Class: 类别 List
        """
        f = codecs.open(path, 'r', encoding='utf-8')
        pattern_Object = re.compile(r'    <owl:ObjectProperty rdf:about="(.*#)(.*)"')
        pattern_Datatype = re.compile(r'    <owl:DatatypeProperty rdf:about="(.*#)(.*)"')
        pattern_Class = re.compile(r'    <owl:Class rdf:about="(.*#)(.*)"')
        byt = f.readlines()
        list_Object = []
        list_Datatype = []
        list_Class = []
        for connent in byt:
            connent = str(connent)
            match_Object = pattern_Object.match(connent)
            match_Datatype = pattern_Datatype.match(connent)
            match_Class = pattern_Class.match(connent)
            if match_Object:
                list_Object.append(match_Object.group(2))
            elif match_Datatype:
                list_Datatype.append(match_Datatype.group(2))
            elif match_Class:
                list_Class.append(match_Class.group(2))
        return list_Object, list_Datatype, list_Class


    def dic_update(self, path, new_dic, start, end):
        """重新填装dic
        @param path: owl文件路径
        @param new_dic: 更新后的owl文件
        @param start: owl文件读写起点ind_start
        @param end: owl文件读写起点ind_end
        """
        f_read = codecs.open(path, 'r', encoding='utf-8')
        byt = f_read.readlines()
        f_read.close()
        connents = []
        for i in new_dic:
            connents += new_dic[i]
        new_byt = byt[:start] + connents + byt[end:]

        f_write = codecs.open(path, 'w', encoding='utf-8')
        for i in new_byt:
            f_write.write(i)
        f_write.close()


    def get_class_inds(self, dic, target):
        """获取目标类下的所有实体
        @param dic: owl字典 dic
        @param target: 要查询的实体类别 list
        @return:
        """
        new_dic = {}
        for i in dic:
            for connent in dic[i]:
                match = re.match(r'        <rdf:type rdf:resource="(.*)#(.*)"/>', connent)
                if match:
                    if match.group(2) in target:
                        new_dic[i] = dic[i]
        return new_dic

    def add_web_ind(self, dic, ind_name, ind_dic, owl_type, subClass):
        ind = ['    \n', '\n', '\n', '    <!-- http://www.owl-ontologies.com/%s.owl#%s -->\n'%(owl_type, ind_name), '\n', '    <owl:NamedIndividual rdf:about="http://www.owl-ontologies.com/%s.owl#%s">\n'%(owl_type, ind_name), '        <rdf:type rdf:resource="http://www.owl-ontologies.com/%s.owl#%s"/>\n'%(owl_type,subClass), '    </owl:NamedIndividual>\n']
        if(len(ind_dic["introduction"])>0):
            ind.insert(6, '        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">%s</rdfs:comment>\n'%(ind_dic["introduction"]))
        if(len(ind_dic["attributes"])>0):
            for attribute in ind_dic["attributes"].keys():
                ind.insert(6, '        <%s rdf:datatype="http://www.w3.org/2001/XMLSchema#string">%s</%s>\n'%(
                    attribute, ind_dic["attributes"][attribute], attribute))
        if (len(ind_dic["relation"]) > 0):
            for rel in ind_dic["relation"].keys():
                ind.insert(6, '<%s rdf:resource="http://www.owl-ontologies.com/Personage.owl#%s"/>\n' % (
                    rel, ind_dic["relation"][rel]))
        dic[ind_name] = ind
        return dic

    def del_class_inds(self, dic, target):
        """删除目标类下的所有实体
          @param dic: owl字典 dic
          @param target: 要操作的实体类别 list
          @return: update后的字典 dic
        """
        l = list(dic)
        for i in dic:
            for connent in dic[i]:
                match = re.match(r'        <rdf:type rdf:resource="(.*)#(.*)"/>', connent)
                if match:
                    if match.group(2) in target:
                        l.remove(i)
        new_dic = {}
        for i in l:
            new_dic[i] = dic[i]
        return new_dic


    def del_inds(self, dic, target):
        """删除目标类下的指定实体
        @param dic: owl字典 dic
        @param target: 要操作的实体列表 list
        @return: update后的字典 dic
        """
        for ind in target:
            if(ind in dic.keys()):
                dic.pop(ind)
        return dic


    def del_inds_data(self, dic, inds, target):
        """删除目标类下的指定实体的某个关系、属性
        @param dic: owl字典 dic
        @param inds: 要操作的实体列表 list
        @param target: 属性名、关系名或者链接对象名 string
        @return: update后的字典 dic
        """
        for ind in inds:
            if (ind in dic.keys()):
                for dataItem in dic[ind]:
                    if target in dataItem:
                        dic[ind].remove(dataItem)
        return dic