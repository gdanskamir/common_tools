#!/usr/bin/env python
#-*- coding:UTF-8 -*-

#################################################
# 文本处理
# Author : gdanskamir
# Date   : 2016-03-11
# HomePage : http://www.cnblogs.com/gdanskamir
#################################################

## @brief: jaccard相似度
def jaccard_similarity(str1, str2):
    str1 = unicode_encode(str1)
    str2 = unicode_encode(str2)
    overlap_cnt = 0
    for word in str1:
        if word in str2:
            overlap_cnt += 1
    return float(overlap_cnt) / (len(str1)+len(str2)-overlap_cnt)
