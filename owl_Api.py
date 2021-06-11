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
    def ind_update(self, path, new_dic, start, end):
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