# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.Config import UserAgent
from Lib.Parser import IP138Parser

import requests as rq
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class ProxyChecker:
    
    @staticmethod
    def getAvailableIP( ip, avIPS ):
        url = 'http://2017.ip138.com/ic.asp'
        headers = { "User-Agent": UserAgent.getUA() }
        proxies = { 'http': 'http://' + ip['IP'] + ':' + ip['PORT'] }
        r = rq.get( url, headers = headers, proxies = proxies, timeout = 10 )
        html = r.content.decode( 'gb2312' )
        if ip['IP'] == IP138Parser.parseDocument( html ):
            avIPS.append( ip )
        
    @staticmethod
    def getAvailableIPTables( ips ):
        print("getAvailableIPTables")
        avIPS = []
        with ThreadPoolExecutor( max_workers = 256 ) as ThreadPool :
            fu_list = []
            for ip in ips:
                fu_list.append( ThreadPool.submit( ProxyChecker.getAvailableIP, ip, avIPS ) )
            for fu in as_completed( fu_list ) :
                pass
        return avIPS