# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    数据库IP检测Worker，定时清理无效IP
'''

from Lib.DBHelper import DBHelper
from Lib.Checker import ProxyChecker
from Lib.AutoLock import AutoLock

class DBCheckerWrapper:
    
    def __init__( self ):
        with AutoLock( 'ippool_dbchecker' ) as lock:
            with DBHelper() as db:
                ips = db.getAllIP()
                avIPS = ProxyChecker.getAvailableIPTables( ips )
                for ip in avIPS:
                    if not ip['ABLE']:
                        db.delIPByID( ip['id'] )
                del ips[ : ]
                del avIPS[ : ]