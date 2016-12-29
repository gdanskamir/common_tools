#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
import re;


dict = ['自治区', '特区', '特别行政区', '自治旗', '自治县', '自治市', '自治州', '林场', '地区', '市', '县', '省', '区', '旗', '盟', '州']


for line in sys.stdin:
    line_str = line.strip();
    print line_str;
    for item in dict:
        item_len = len(item);
        line_str_len = len(line_str);
        if line_str.endswith(item) == True:
            print line_str[0:line_str_len-item_len]
            break;

