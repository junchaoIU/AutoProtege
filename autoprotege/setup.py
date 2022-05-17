from setuptools import setup, find_packages            #这个包没有的可以pip一下


setup(name='autoprotege',
      version='2.0.0',
      keywords = ["protege", "ontology"],			# 关键字
      description="A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege",
      author='wujunchao',
      url = "https://github.com/junchaoIU/AutoProtege",
      author_email='wujunchaoIU@outlook.com',
      requires= ['numpy'], # 定义依赖哪些模块
      packages = find_packages(),  # 系统自动从当前目录开始找包
      # 如果有的文件不用打包，则只能指定需要打包的文件
      #packages=['代码1','代码2','__init__']  #指定目录中需要打包的py文件，注意不要.py后缀
      license="Mozilla Public License Version 2.0"
      )