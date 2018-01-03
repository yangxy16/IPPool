# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Config import WebConf, DBConf
from Parser import XiCiParser, IP181Parser, KuaiIPParser, Data5UParser

import requests as rq
import time
import json
import threading

class ProxyChecker:
    
    @staticmethod
    def checkAvailable( ip, port ):
        return True

class Crawler:
    
    @staticmethod
    def getProxyIP():
        ips = []
        headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36" }
        
        def getIP181( ips ):
            for url in WebConf.IP181:
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'gb2312' )
                    ips.extend( IP181Parser.parseDocument( html ) )
                time.sleep( 0.5 )
                
        def getXC( ips ):
            for url in WebConf.XICI:
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    ips.extend( XiCiParser.parseDocument( html ) )
                time.sleep( 0.5 )
        
        def getKUAI( ips ):
            for url in WebConf.KUAIIP:
                r = rq.get( url, headers = headers )
                if r.status_code == 200:
                    html = r.content.decode( 'utf-8' )
                    ips.extend( KuaiIPParser.parseDocument( html ) )
                time.sleep( 0.5 )
        
        def get5U( ips ):
            for url in WebConf.DATA5U:
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

        return ips
        
if __name__ == '__main__':
    with open( "iplist.txt", "wb" ) as f:
        for ip in Crawler.getProxyIP():
            ip = json.dumps( ip, ensure_ascii = False )
            f.write( bytes( ip, 'utf-8' ) )
            f.write( b'\r\n' )