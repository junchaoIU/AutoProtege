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

# 最常用的，获取所有owl实体并转换为字典dic，修改字典dic即可，另外两个start和end用来定位的，不用管
dic, ind_start, ind_end = owl_model.get_individuals_dic(owl_path)
print(ind_start)
print(ind_end)
print(dic)

