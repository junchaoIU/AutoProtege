# -------------------------------------------------------------------------------
# Description:  
# Reference:
# Name:   test
# Author: wujunchao
# Date:   2021/6/10
# -------------------------------------------------------------------------------

from owl_Api import *

owl_path = r"cantonowl\Event.owl"  # 目标owl地址
owl_model = Parse_Owl()

"""
dic:所有实体集合字典
ind_start:owl读写起点标记
ind_end:owl读写末尾标记
"""
print("\n\n{:*^60}".format("拿到owl文件的实体字典"))
# 最常用的，获取所有owl实体并转换为字典dic，修改字典dic即可，另外两个start和end用来定位的，不用管
dic, ind_start, ind_end = owl_model.get_individuals_dic(owl_path)
print("ind_start:{},int_end:{}".format(ind_start,ind_end))
print("owl字典:{}".format(owl_model.standard_dic(dic)))
print("owl实体集合:{}".format(dic.keys()))
#
# print("\n\n{:*^60}".format("拿到owl文件的实体信息"))
# list_Object, list_Datatype, list_Class = owl_model.get_individuals_ins(owl_path)
# print("owl实体关系类别:{}".format(list_Object))
# print("owl实体属性类别:{}".format(list_Datatype))
# print("owl实体类别:{}".format(list_Class))
#
# print("\n\n{:*^60}".format("拿到指定类的实体字典"))
# # #拿到指定类的实体字典
# for subClass in list_Class:
#     wzdz_dic = owl_model.get_class_inds(dic,[subClass])
#     print(subClass+"实体数量:{}".format(len(wzdz_dic.keys())))
#     print(subClass+"实体集合:{}".format(wzdz_dic.keys()))
#     print(subClass + "dic:{}".format(owl_model.standard_dic(wzdz_dic))+"\n")
#
# print("\n\n{:*^60}".format("删除指定类的实体字典"))
# delwzdz_dic = owl_model.del_class_inds(dic,['罢工游行'])
# print("del武装斗争dic:{}".format(delwzdz_dic))
# print("del武装斗争的实体集合:{}".format(delwzdz_dic.keys()))

# print("\n\n{:*^60}".format("删除指定实体"))
# del_inds_List = ['中山舰事件']
# del_inds_dic = owl_model.del_inds(dic,del_inds_List)
# print("删除{}后的实体集合:{}".format(del_inds_List,del_inds_dic.keys()))

# print("\n\n{:*^60}".format("删除指定实体的某个属性或关系"))
# del_inds_List = ['大隧道惨案']
# target = "开始时间"
# del_indsData_dic = owl_model.del_inds_data(dic, del_inds_List,target)
# print("删除{}的{}后的dic:{}".format(del_inds_List, target, owl_model.standard_dic(del_indsData_dic)))
#
# # 修改完dic后再用这个就可以更新owl（注意，使用这个函数前最好备份一份owl，以防出错）
# print("\n\n{:*^60}".format("更新删除指定类后的实体字典"))
# new_dic = owl_model.dic_update(owl_path,del_indsData_dic,ind_start,ind_end)