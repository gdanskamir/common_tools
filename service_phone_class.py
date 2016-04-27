#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import sys;
import json;
import re;
from common import *

reload(sys);
sys.setdefaultencoding('UTF-8');

class service_phone_class:
    telOrMob = 0;       ##默认电话
    remark = "";
    areaNo = "";        ##区号
    phoneNo = "";       ##
    extensionNo = "";   ##分机号
    carrierOperator = "";##运营商
    supportBusiness = [];
    isFax = 0;

    def __init__(self):
        self.do_init();

    def do_init(self):
        self.telOrMob = 0;       ##默认电话
        self.remark = "";
        self.areaNo = "";        ##区号
        self.phoneNo = "";       ##
        self.extensionNo = "";   ##分机号
        self.carrierOperator = "";##运营商
        self.supportBusiness = [];
        self.isFax = 0;

    def parser(self, str, phone_prefix, mobile_prefix_dict, idx, no):
        if no[0:2] in mobile_prefix_range:
            no = no.replace('-', '');
            if len(no) != 11:
                return -1
            if no[0:3] in mobile_prefix_dict:
                self.carrierOperator = mobile_prefix_dict[no[0:3]];
            elif no[0:4] in mobile_prefix_dict:
                self.carrierOperator = mobile_prefix_dict[no[0:4]];
            else:
                sys.stderr.write('mobile prefix error, no:' + no  + "\n");
                return -1;
            self.telOrMob = 1;
            self.phoneNo = no.replace('-', '');
        else:
            if no.find('-') != -1:
                str_prefix = no.split('-')[0];
                if len(str_prefix) >= 1 and str_prefix[0] != '0':
                    str_prefix = "0" + str_prefix;
                if str_prefix != phone_prefix:
                    sys.stderr.write('phone_prefix error, no:' + no  + " phone_prefix:" + phone_prefix+"\n");
                    return -1;
                self.telOrMob = 0;
                self.areaNo = phone_prefix;
                self.phoneNo = no.split('-')[1];
            elif no.find(phone_prefix) == 0 or ("0"+no).find(phone_prefix) == 0:
                self.telOrMob = 0;
                self.areaNo = phone_prefix;
                self.phoneNo = no[len(phone_prefix):]
            elif len(no) == 7 or len(no) == 8:
                self.telOrMob = 0;
                self.areaNo = phone_prefix;
                self.phoneNo = no;
        ##service
        for i in service_list:
            if str.find(i) != -1:
                self.supportBusiness.append(i);
        return 0;


    def format(self):
        out = {};
        out["telOrMob"] = self.telOrMob;
        out["remark"] = self.remark;
        out["areaNo"] = self.areaNo;
        out["phoneNo"] = self.phoneNo;
        out["extensionNo"] = self.extensionNo;
        out["carrierOperator"] = self.carrierOperator;
        out["supportBusiness"] = self.supportBusiness;
        out["isFax"] = self.isFax;
        return out
