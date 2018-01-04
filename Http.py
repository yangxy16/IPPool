# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    整个架构中，HTTP服务属于细枝末节的东西，所以简单实现了，通过ab做了简单的压测，对一般的分布式爬虫来说QPS够用了
'''

from Lib.HttpWrapper import HttpWrapper

if __name__ == '__main__':
    HttpWrapper()