#!/usr/bin/env python
#-*- coding:UTF-8 -*-

#################################################
# 各种距离计算
# Author : gdanskamir
# Date   : 2016-02-18
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

## @brief:cos相似度
def cosine_similarity(vec1, vec2):
    if len(vec1)==0 or len(vec2)==0 or len(vec1) != len(vec2):
        return 0
    cross = 0.0
    norm_vec1 = 0.0
    norm_vec2 = 0.0
    for i in range(len(vec1)):
        cross += float(vec1[i]) * float(vec2[i])
        norm_vec1 += float(vec1[i]) * float(vec1[i])
        norm_vec2 += float(vec2[i]) * float(vec2[i])
    norm = (math.sqrt(norm_vec1) * math.sqrt(norm_vec2))
    cross = cross / norm if norm > 1e-6 else 0.0
    return round(cross, 4)

## @brief: 编辑距离
def levenshtein_similarity(str_1, str_2):
    str_1 = str_1.decode('UTF-8', 'ignore');
    str_2 = str_2.decode('UTF-8', 'ignore');
    len_1 = len(str_1) + 1;
    len_2 = len(str_2) + 1;

    ##判断空字符串
    if len_1 == 1:
        return len_2 -1
    if len_2 == 1:
        return len_1 -1

    matrix = [range(len_1) for x in range(len_2)]
    for i in range(1,len_2):
        matrix[i][0] = i
    for i in range(1,len_2):
        for j in range(1,len_1):
            deletion = matrix[i-1][j]+1
            insertion = matrix[i][j-1]+1
            substitution = matrix[i-1][j-1]
            if str_2[i-1] != str_1[j-1]:
                substitution += 1
            matrix[i][j] = min(deletion,insertion,substitution)
    return matrix[len_2-1][len_1-1]


