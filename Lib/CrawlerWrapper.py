# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    代理IP抓取Worker
'''

from Lib.Config import WebConf, UserAgent
from Lib.Parser import XiCiParser, IP181Parser, KuaiIPParser, Data5UParser
from Lib.Checker import ProxyChecker
from Lib.AutoLock import AutoLock
from Lib.DBHelper import DBHelper

import requests as rq
import time
import json
import threading

class Crawler:
    
    @staticmethod
    def getProxyIP():
        ips = []

        def getIP181( ips ):
            for url in WebConf.IP181:
                headers = { "User-Agent": UserAgent.getUA() }
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'gb2312' )
                    ips.extend( IP181Parser.parseDocument( html ) )
                time.sleep( 0.5 )

        def getXC( ips ):
            for url in WebConf.XICI:
                headers = { "User-Agent": UserAgent.getUA() }
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    ips.extend( XiCiParser.parseDocument( html ) )
                time.sleep( 0.5 )
        
        def getKUAI( ips ):
            for url in WebConf.KUAIIP:
                headers = { "User-Agent": UserAgent.getUA() }
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    ips.extend( KuaiIPParser.parseDocument( html ) )
                time.sleep( 0.5 )
        
        def get5U( ips ):
            for url in WebConf.DATA5U:
                headers = { "User-Agent": UserAgent.getUA() }
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    ips.extend( Data5UParser.parseDocument( html ) )
                time.sleep( 0.5 )
        
        hThreadTbl = [
                        threading.Thread( target = getIP181, args = ( ips, ) ),
                        threading.Thread( target = getXC, args = ( ips, ) ),
                        threading.Thread( target = getKUAI, args = ( ips, ) ),
                        threading.Thread( target = get5U, args = ( ips, ) )
                    ]
        
        for hThread in hThreadTbl:
            hThread.start()
        
        for hThread in hThreadTbl:
            hThread.join()
            
        del hThreadTbl[ : ]
        
        #清理重复IP
        ipsNonDuplicate = ProxyChecker.duplicateRemoveIPTables( ips )
        del ips[ : ]
        
        #检测IP可用性返回可用IP列表
        avIPS = ProxyChecker.getAvailableIPTables( ipsNonDuplicate )
        return avIPS
        
class CrawlerWrapper:
    
    def __init__( self ):
        with AutoLock( 'ippool_crawler' ) as lock:
            avIPS = Crawler.getProxyIP()
            with DBHelper() as db:
                for ip in avIPS:
                    if ip['ABLE']:
                        db.addIP( ip['ip'], ip['port'], ip['hash'] )
            del avIPS[ : ]