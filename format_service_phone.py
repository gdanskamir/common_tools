#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import json
import re;
import sys;
from common import *
from service_phone_class import *
from service_phone_package import *

reload(sys);
sys.setdefaultencoding('UTF-8');


phone_area_filename="/home/disk0/wangbo01/import-data/phone/telephone_area_code"
mobile_prefix_filename="/home/disk0/wangbo01/import-data/phone/mobilephone"
china_nation_filename="/home/disk0/wangbo01/import-data/phone/china_nation"
service_phone_manager = service_phone_package();
service_phone_manager.load_dicts(phone_area_filename, mobile_prefix_filename, china_nation_filename)
for line in sys.stdin:
    if line.strip() == "":
        continue;
    
    data_arr = json.loads(line.rstrip());
    service_phone_manager.do_init();
    sys.stdout.write(str(data_arr["data"]['phone']).replace('\t', ';').encode('UTF-8')+"\t"+data_arr["data"]['province'].encode('UTF-8')+"\t"+data_arr["data"]['city'].encode('UTF-8')+"\t"+data_arr["data"]['address'].encode('UTF-8') + "\t");
    service_phone_manager.do_process(str(data_arr["data"]['phone']).replace('\t', ';').encode('UTF-8'), data_arr["data"]['province'].encode('UTF-8'), data_arr["data"]['city'].encode('UTF-8'), data_arr["data"]['address'].encode('UTF-8'))
    print json.dumps(service_phone_manager.do_format(False), ensure_ascii=False)

