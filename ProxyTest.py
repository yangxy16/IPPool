# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    代理测试
'''

import requests as rq

if __name__ == '__main__':
    ip = '120.77.201.46'
    port = '8080'
    
    def getAvailableIP( ip, port ):
        url = 'http://2017.ip138.com/ic.asp'
        proxies = { 'http': 'http://' + ip + ':' +  port }
        try:
            r = rq.get( url, proxies = proxies, timeout = 10 )
            if r.status_code == 200:
                html = r.content.decode( 'gb2312' )
                print( html )
            else:
                print( r.status_code )
        except Exception as e:
            print( e )
            
    getAvailableIP( ip, port )