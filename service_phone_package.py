#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
import json;
import re;
from common import *
from service_phone_class import *

reload(sys);
sys.setdefaultencoding('UTF-8');


class service_phone_package:
    items = [];
    str_input = "";
    token_seg = [];
    phone_area_dict = {};
    mobile_prefix_dict = {};
    province = "";
    city = "";
    address = "";
    china_nation_list = [];


    def __init__(self):
        self.do_init();
    
    def do_init(self):
        del self.items[:];
        del self.token_seg[:];
        self.province = "";
        self.city = "";
        self.address = "";
        self.str_input = "";

    def load_dicts(self, phone_area_filename, mobile_prefix_filename, china_nation_filename):
        for line in open(phone_area_filename):
            token_list = line.strip().split('\t');
            if token_list[1] == "":
                self.phone_area_dict[token_list[0].strip()] = token_list[2];
            else:
                self.phone_area_dict[token_list[0].strip() + ":" + token_list[1].strip()] = token_list[2];

        for line in open(mobile_prefix_filename):
            token_list = line.strip().split('\t');
            self.mobile_prefix_dict[token_list[0]] = token_list[1];
    
        for line in open(china_nation_filename):
            self.china_nation_list.append(line.strip());
    
    def format_province(self, str):
        if str[-3:] == "市":
            return str[0:-3];
        elif str[-3:] == "省":
            return str[0:-3];
        elif str[-6:] == "地区":
            return str[0:-6];
        elif str[-3:] == "县":
            return str[0:-3];
        elif str[-3:] == "盟":
            return str[0:-3];
        else:
            for nation_item in self.china_nation_list:
                if nation_item == "维吾尔族": nation_item = "维吾尔";
                if nation_item == "哈萨克族": nation_item = "哈萨克";
                pos = str.find(nation_item + "自治");
                if pos != -1:
                    return str[0:pos];

            if str[-3:] == "州" and len(str) >= 9:
                return str[0:-3];
            if str[-9:] == "自治区":
                return str[0:-9];
        return str;


    def do_process(self, str, province, city, address):
        self.str_input = strQ2B(str.strip().decode('UTF-8', 'ignore')).encode('UTF-8', 'ignore');
        self.str_input = self.str_input.replace('；', ';').replace('，', ',').replace('--', '-');
        idx = 0;
        self.token_seg = re.split(';|；|,|、|，', self.str_input)
        
        self.province = province;
        self.city = city;
        self.address = address;
        phone_prefix = "";

        self.province = self.format_province(self.province);
        self.city = self.format_province(self.city);

        key = self.province + ":" + self.city;
        if key in self.phone_area_dict:
            phone_prefix = self.phone_area_dict[key];
        elif self.province in self.phone_area_dict:
            phone_prefix = self.phone_area_dict[self.province];
        else:
            sys.stderr.write("province error info:" + province + "\t" + city + "\t" + address + "\t-->" + self.province + "\t" +  self.city+"\n")
            return;
                
        phone_prefix_len = len(phone_prefix)
        while idx < len(self.token_seg):

            ret_all = big_pat.findall(self.token_seg[idx]);
            idx_inner = 0;
            for item in ret_all:
                no = item.encode('UTF-8', 'ignore');
                pos = self.token_seg[idx].find(no, idx_inner);
                if pos == -1:
                    continue;
                else:
                    idx_inner = pos + 1;

                item = service_phone_class();
                ret = item.parser(self.token_seg[idx], phone_prefix, self.mobile_prefix_dict, pos, no);
                if ret == 0:
                    self.items.append(item);
                #print "token->" + self.token_seg[idx] + "\tstr_org->" + str + "\tphone_no->" + no
            idx = idx + 1;
        return ;

    def do_format(self, is_rest):
        out_arr = [];
        if is_rest == False:
            for item in self.items:
                out_arr.append(item.format())
        else:
            for item in self.items_rest:
                out_arr.append(item.format());
        return out_arr;

