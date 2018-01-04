# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.Config import DBConf
import pymysql.cursors

class DBHelper:
    def __enter__( self ):
        self.connection = pymysql.connect( host = DBConf.IP, port = DBConf.PORT, 
                                            user = DBConf.User, password = DBConf.PassWord, 
                                            db = DBConf.DBName, charset = 'utf8mb4', 
                                            cursorclass = pymysql.cursors.DictCursor )
                                            
    def __exit__( self, type, value, trace ):
        self.connection.close()
        
        
        
'''
sql_id = 'SELECT id,uid FROM ls_case_id WHERE uid in ({})'.format(idStrList)
    connection = pymysql.connect( host = '10.96.92.41', port = 3307, user = 'wx_case_info', password = 'ha1or2en3', db = 'wx_case_info', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor )
    result = None
    try :
        with connection.cursor() as cursor :
            cursor.execute( sql_id )
            ls_case_id = cursor.fetchall()
            result = {}
            for v in ls_case_id:
                result[v['uid']] = int(v['id']) % 100
    except:
        result = None
    finally :
        connection.close()
    return result

'''