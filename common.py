#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import sys;
import json;
import re;


service_list = ["对私", "对公"]


mobile_prefix_range = set(['13', '14', '15', '16', '17', '18'])
no_pat = re.compile('((1[3-8][0-9]{9})|([0-9]{7,8}))');


big_pat = re.compile('([01234567890-]{7,25})');



