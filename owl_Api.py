# -------------------------------------------------------------------------------
# Description:  
# Reference:  正式Api文件
# Name:   owl_Api
# Author: wujun
# Date:   2021/6/11
# -------------------------------------------------------------------------------
import codecs
import re
import os

class Parse_Owl:
    # 获得所有实体块字典dic
    def get_individuals_dic(self, path):
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

    # 重新填装dic
    def dic_update(self, path, new_dic, start, end):
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

    # 获取目标类下的所有实体
    def get_class_inds(self, dic, target):
        new_dic = {}
        for i in dic:
            for connent in dic[i]:
                match = re.match(r'        <rdf:type rdf:resource="(.*)#(.*)"/>', connent)
                if match:
                    if match.group(2) in target:
                        new_dic[i] = dic[i]
        return new_dic

    # 删除目标类下的所有实体
    # 修改完dic后再用这个就可以更新owl（注意，使用这个函数前最好备份一份owl，以防出错）
    def del_class_inds(self, dic, target):
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