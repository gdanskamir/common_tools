#!/usr/bin/env python
#-*- coding:UTF-8 -*- 

import sys
import log
import logging
import similarity_compute
import marisa_trie
from langconv import *


log.init_log('./log/common_tools')
logging.info("test levenshtein")
print similarity_compute.levenshtein_similarity("1234", "562888")

logging.info("trie tree")
data_list = ["asdfasf", "adsfs", "123", "as"]
data_list_decode = [i.decode('UTF-8', 'ignore') for i in data_list];
print data_list_decode;
marisa_trie = marisa_trie.Trie(data_list_decode);
print True if u'as' in marisa_trie else False;
print marisa_trie.prefixes(u'as');
print marisa_trie.keys(u"as")
print marisa_trie.items()
print marisa_trie.items(u"as")

# 转换繁体到简体
line="中華人名共和國"
line = Converter('zh-hans').convert(line.decode('utf-8'))
line = line.encode('utf-8')
print line;
# 转换简体到繁体
line="中华人民共和国"
line = Converter('zh-hant').convert(line.decode('utf-8'))
line = line.encode('utf-8')
print line;
