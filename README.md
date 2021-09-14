[![author](https://img.shields.io/badge/Author-WuJunchao-purple)](https://github.com/junchaoIU)
[![license](https://img.shields.io/badge/license-MPL2.0-blue)](https://github.com/junchaoIU/protegeAuto_tool/blob/main/LICENSE)
[![protege](https://img.shields.io/badge/protege-5.5.0-yellowgreen)](https://github.com/protegeproject/protege)
[![python](https://img.shields.io/badge/Python-3.7.6-orange)](https://github.com/TheAlgorithms/Python)


## 🌈简介
🎉  protegeAuto_tool
- protegeAuto_tool是一个面向斯坦福大学研发的开源本体构建工具protege而开发的python操作包
- 基于protegeAuto_tool可以打破传统手工构建本体库的局限，实现本体数据的批量增改和查询等操作，更为灵活
- 不基于SPARSQL 进行检索，降低了学习成本
- 尽量涵盖基础接口，满足交叉领域学者的本体构建需求
- 在功能完善的基础上进行轻量化，便于用户根据项目需求二次开发
- 版权归北京师范大学珠海分校管理学院广州革命历史知识图谱团队所有
- 供与学术研究使用 有什么新功能需求可提issue，会在后续陆续更新

> PS:目前V1.0.0 版本还未更新完毕，代码的整理及完善需要时间，预计2021年底发布第一个版本，欢迎各位protege的使用者可以期待&关注一下

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

> 广州革命历史数字图书馆
> 系统前端：https://github.com/junchaoIU/Canton-KG-React
> 系统后端：https://github.com/Chen-X666/canton
