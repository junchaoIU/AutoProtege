[![author](https://img.shields.io/badge/Author-WuJunchao-purple)](https://github.com/junchaoIU)
[![license](https://img.shields.io/badge/license-MPL2.0-blue)](https://github.com/junchaoIU/protegeAuto_tool/blob/main/LICENSE)
[![protege](https://img.shields.io/badge/protege-5.5.0-yellowgreen)](https://github.com/protegeproject/protege)
[![python](https://img.shields.io/badge/Python-3.7.6-orange)](https://github.com/TheAlgorithms/Python)


## 🌈简介
🎉  protegeAuto_tool
- protegeAuto_tool是一个面向斯坦福大学研发的开源本体构建工具protege而开发的python操作包
- 基于protegeAuto_tool可以打破传统手工构建本体库的局限，实现本体数据的批量增改和查询等操作，更为灵活
- 版权归北京师范大学珠海分校管理学院广州革xian命历史知识图谱团队所有

> PS:目前V1.0 版本还未更新完毕，代码的整理及完善需要时间，预计2021年底发布第一个版本，欢迎各位protege的使用者可以期待&关注一下。
> 另外正在设计protege的 mangoDB映射版本，基于JSON管理的mangoDB可以更好的减少专家学者对于RDFS/OWL知识框架相关工具的学习成本。

## 进程说明
- 最近收到了不少人的邮箱私信，希望我们尽快发布V1.0版本，于是近日进行了部分工作的整理update，以下为部分已做和计划做的功能：
### 实体查询
- [x] 查子类
- [x] 查某个子类下所有实体
- [x] 查某个实体的所有信息
### 实体更新
- [x] 加某个类下的实体信息
- [ ] 加某个实体的时空线
- [ ] 加某个类下的实体单个关系
- [ ] 加某个类下的实体单个属性
### 实体删除
- [x] 删除某个类下的所有实体
- [x] 删除单个实体所有信息
- [x] 删除某个实体下的某个关系
- [x] 删除某个实体下的某个属性

## 🖥 第三方库
- codes
- re
- os

## 📦 快速使用
```shell
# 克隆项目
git clone https://github.com/junchaoIU/protegeAuto_tool.git
# 进入项目目录
cd protegeAuto_tool
```

```python
# 第一个例子
from owl_Api import *

# 要操作的本体文件
owl_path = r"cantonowl\Event.owl"  # 目标owl地址
# 定义本体模型
owl_model = Parse_Owl()

# 最常用的，获取所有owl实体并转换为字典dic，修改字典dic即可，另外两个start和end用来定位的，不用管
dic, ind_start, ind_end = owl_model.get_individuals_dic(owl_path)
print(dic)
```

## 🌸关于作者
🍧 Wu, Junchao 

> 有什么问题请致邮：wujunchaoIU@outlook.com,我会第一时间为你解答

- 个人博客：[🌸 春天与爱情の樱花](https://www.wujunchao.top)
- 博客园：[🌸 梦淑の博客园](http://cnblogs.wujunchao.top)
- 语雀：[🌸 CCの知识库](https://www.yuque.com/wujunchao)

> 项目的开发和维护需要花费较多的时间，如果我的项目对你有帮助，如果你对我的项目感兴趣,请帮我点个小星星star，感激！🍉

## 其他：
> 如果你对该项目感兴趣的话，欢迎了解项目的一些详细内容：
> 该项目阶段性成果论文1：
> - J. Wu, Y. Jiang, X. Chen, et al. "The Canton Canon" Digital Library Based on Knowledge
Graph - Taking the Revolutionary Archives of Canton in the Republic of China as an Example. [C]// 2021 10th International Conference on Educational and Information Technology (ICEIT),2021: 171-179.
> - DOI: 10.1109/ICEIT51700.2021.9375538
> - 索引平台：IEEE, EI, scopus

> 该项目阶段性成果论文2：
> - 基于知识图谱的民国革命历史时空模型构建与应用
> - （在投）

> 项目的其他核心代码会逐渐开源（包括本体构建等）
