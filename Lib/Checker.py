# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    清理重复IP、检测可用IP封装
'''

from Lib.Config import UserAgent
from Lib.Parser import IP138Parser

import requests as rq
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class ProxyChecker:

    @staticmethod
    def duplicateRemoveIPTables( ips ):
        kmap = {}
        ipsNonDuplicate = []
        for ip in ips:
            if not kmap.get( ip['hash'], None ):
                ipsNonDuplicate.append( ip )
                kmap[ip['hash']] = 1
        kmap.clear()
        return ipsNonDuplicate
     
    @staticmethod
    def getAvailableIPTables( ips ):
        def getAvailableIP( ip ):
            ip['ABLE'] = False
            url = 'http://2017.ip138.com/ic.asp'
            headers = { "User-Agent": UserAgent.getUA() }
            proxies = { 'http': 'http://' + ip['ip'] + ':' + str( ip['port'] ) }
            try:
                r = rq.get( url, headers = headers, proxies = proxies, timeout = 10 )
                if r.status_code == 200:
                    html = r.content.decode( 'gb2312' )
                    ip['ABLE'] = ( ip['ip'] == IP138Parser.parseDocument( html ) )
            except:
                ip['ABLE'] = False

        with ThreadPoolExecutor( max_workers = 256 ) as ThreadPool :
            fu_list = []
            for ip in ips:
                fu_list.append( ThreadPool.submit( getAvailableIP, ip ) )
            for fu in as_completed( fu_list ) :
                pass
        return ips