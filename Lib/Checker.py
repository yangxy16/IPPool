# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.Config import UserAgent
from Lib.Parser import IP138Parser

import requests as rq
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class ProxyChecker:
     
    @staticmethod
    def getAvailableIPTables( ips ):
    
        def getAvailableIP( ip, avIPS ):
            url = 'http://2017.ip138.com/ic.asp'
            headers = { "User-Agent": UserAgent.getUA() }
            proxies = { 'http': 'http://' + ip['IP'] + ':' + ip['PORT'] }
            try:
                r = rq.get( url, headers = headers, proxies = proxies, timeout = 10 )
                html = r.content.decode( 'gb2312' )
                if ip['IP'] == IP138Parser.parseDocument( html ):
                    avIPS.append( ip )
            except:
                pass
        
        def duplicateRemove( ips ):
            kmap = {}
            ipsNonDuplicate = []
            for ip in ips:
                if not kmap.get( ip['HASH'], None ):
                    ipsNonDuplicate.append( ip )
                    kmap[ip['HASH']] = 1
            kmap.clear()
            return ipsNonDuplicate
    
        ipsNonDuplicate = duplicateRemove( ips )
        del ips[ : ]
        avIPS = []
        with ThreadPoolExecutor( max_workers = 256 ) as ThreadPool :
            fu_list = []
            for ip in ipsNonDuplicate:
                fu_list.append( ThreadPool.submit( getAvailableIP, ip, avIPS ) )
            for fu in as_completed( fu_list ) :
                pass
        del ipsNonDuplicate[ : ]
        return avIPS