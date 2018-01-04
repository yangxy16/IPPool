# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    数据库IP检测Worker，定时清理无效IP
'''

from Lib.DBCheckerWrapper import DBCheckerWrapper

if __name__ == '__main__':
    DBCheckerWrapper()