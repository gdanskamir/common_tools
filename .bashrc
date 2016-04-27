#!/bin/bash

## HADOOP ?ͻ???
export hadoop_rp=/home/disk0/wangbo01/hadoop-client-dir/hadoop-client-rp/hadoop/bin/hadoop
#export hadoop_hlb=/home/spider/wangbo01/hadoop-client-dir/hadoop-client-hlb/hadoop/bin/hadoop
export hadoop_nj=/home/disk0/wangbo01/hadoop-client-dir/hadoop-client-wdm-link-offline/hadoop/bin/hadoop
export hadoop_kg=/home/disk0/wangbo01/hadoop-client-dir/hadoop-client-wdm-entities-off/hadoop/bin/hadoop

alias ccdb="ssh wangbo01@nj01-ps-ccdb1000.nj01"
alias dev="ssh wangbo01@cq01-ps-dev187.cq01.baidu.com"
alias cm6="ssh spider@szjjh-spi-hlbcm6.szjjh01.baidu.com"
alias wdmlink="ssh wdmlink@cq01-rdqa-pool126.cq01.baidu.com"
alias kgb="ssh spider@nj02-spi-kgb02.nj02.baidu.com"
alias wdm="ssh spider@cq02-wdm-szoff3.cq02.baidu.com"
alias diaoyan3="ssh spider@yq01-kg-diaoyan3.yq01"
##wd123!@#WD
#nj01-ps-ccdb1000.nj01
#cq01-rdqa-pool126.cq01.baidu.com wdmlink
#db-ps-laisp0.db01.baidu.com moc8rats
#szjjh-spi-hlbcm6.szjjh01.baidu.com
#cq01-ps-dev187.cq01.baidu.com 

function get_file_ftp
{
    local file=$1
    echo "ftp://`hostname``readlink -f ${file}`"
}

#export get_file_ftp


export LANG=zh_CN.UTF-8
#alias vim="vim  -u ~/wangbo01/.vimrc"
#alias vi="vim"

export PS1='[\h \[\e[31;40m\]\A \[\e[0m\] \W]\n'

alias sample="sh -x ~/wangbo01/sample.sh "

export PYTHONPATH=$PYTHONPATH:/home/disk0/wangbo01/study/git/scrapy/build/lib/:/home/disk0/wangbo01/study/git/Twisted-15.5.0/build/lib.linux-x86_64-2.7/:/home/disk0/wangbo01/study/git/zope.interface-4.1.3/build/lib.linux-x86_64-2.7/:/home/disk0/wangbo01/study/git/w3lib-1.13.0/build/lib/:/home/disk0/wangbo01/study/git/cssselect-0.9.1/build/lib/:/home/spider/wangbo01/study/git/pyopenssl-master/build/lib/:/home/disk0/wangbo01/study/git/cffi-1.5.2/build/lib.linux-x86_64-2.7/:/home/disk0/wangbo01/study/git/third-package/python/:/home/spider/wangbo01/study/git/common_tools/


export PATH=/home/disk0/wangbo01/study/tmp/mpich-3.2/output/bin:/home/spider/.jumbo/opt/gcc48/bin/:${PATH}
export C_INCLUDE_PATH=/home/disk0/wangbo01/study/tmp/mpich-3.2/output/include/:/home/disk0/wangbo01/study/git/boost/:/home/disk0/wangbo01/study/git/openssl-1.0.2g/output/include/:${C_INCLUDE_PATH}
export CPLUS_INCLUDE_PATH=/home/disk0/wangbo01/study/tmp/mpich-3.2/output/include/:/home/disk0/wangbo01/study/git/boost/:${CPLUS_INCLUDE_PATH}:/home/disk0/wangbo01/study/git/openssl-1.0.2g/output/include/
export LD_LIBRARY_PATH=/home/disk0/wangbo01/study/lightlda/multiverso/third_party/lib/:/home/disk0/wangbo01/study/tmp/mpich-3.2/output/lib/:/home/disk0/wangbo01/study/git/openssl-1.0.2g/output/lib/:${LD_LIBRARY_PATH}
export LIBRARY_PATH=/home/disk0/wangbo01/study/lightlda/multiverso/third_party/lib/:/home/disk0/wangbo01/study/tmp/mpich-3.2/output/lib/:/home/disk0/wangbo01/study/git/boost/stage/lib/:/home/disk0/wangbo01/study/git/openssl-1.0.2g/output/lib/:${LIBRARY_PATH}

export GIT_TRACE_PACKET=1
export GIT_TRACE=1
export GIT_CURL_VERBOSE=1

git config --global http.postBuffer 100M
git config http.postBuffer 102400000
git config --global user.name gdanskamir
git config --global user.email 759575836@qq.com

