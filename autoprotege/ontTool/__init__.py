# -*- coding=utf-8 -*-
"""
# library: autoprotege
# author: wujunchao
# license: Apache License 2.0
# email: wujunchaoIU@outlook.com
# github: https://github.com/junchaoIU/AutoProtege
# description: A Python Operation Tool Developed for Stanford University's Open Source Ontology Construction Tool Protege
"""

from.initial_owl import InitialOwl
from .split_owl import SpiltOwl
from .read_owl import ReadOwl
from .merge_owl import MergeOwl

initial_owl = InitialOwl()
split_owl = SpiltOwl()
read_owl = ReadOwl()
merge_owl = MergeOwl()