# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Config import DBConf, UserAgent
from Parser import IP138Parser

import requests as rq
import time
import threading

class ProxyChecker:
    
    @staticmethod
    def checkAvailable( ip, port ):
        url = 'http://2017.ip138.com/ic.asp'
        headers = { "User-Agent": UserAgent.getUA() }
        proxies = { 'http': 'http://' + ip + ':' + port }
        r = rq.get( url, headers = headers, proxies = proxies, timeout = 10 )
        html = r.content.decode( 'gb2312' )
        return ip == IP138Parser.parseDocument( html )