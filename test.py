# -------------------------------------------------------------------------------
# Description:  
# Reference:
# Name:   test
# Author: wujun
# Date:   2021/6/10
# -------------------------------------------------------------------------------

from owl_Api import *

owl_path = r"cantonowl\Event.owl"  # 目标owl地址
owl_model = Parse_Owl()

print("\n\n{:*^60}".format("拿到owl文件的实体字典"))
# 最常用的，获取所有owl实体并转换为字典dic，修改字典dic即可，另外两个start和end用来定位的，不用管
dic, ind_start, ind_end = owl_model.get_individuals_dic(owl_path)
print("ind_start:{},int_end:{}".format(ind_start,ind_end))
print("owl字典:{}".format(dic))
print("owl实体集合:{}".format(dic.keys()))

print("\n\n{:*^60}".format("拿到指定类的实体字典"))
#拿到指定类的实体字典
wzdz_dic = owl_model.get_class_inds(dic,['武装斗争'])
print("武装斗争dic:{}".format(wzdz_dic))
print("武装斗争实体集合:{}".format(wzdz_dic.keys()))

print("\n\n{:*^60}".format("删除指定类的实体字典"))
delwzdz_dic = owl_model.del_class_inds(dic,['武装斗争'])
print("del武装斗争dic:{}".format(delwzdz_dic))
print("del武装斗争的实体集合:{}".format(delwzdz_dic.keys()))

#修改完dic后再用这个就可以更新owl（注意，使用这个函数前最好备份一份owl，以防出错）
print("\n\n{:*^60}".format("更新删除指定类后的实体字典"))
new_dic = owl_model.dic_update(owl_path,delwzdz_dic,ind_start,ind_end)
print("更新后的owl字典:{}".format(new_dic))
print("更新后的owl字典实体集合:{}".format(new_dic.keys()))