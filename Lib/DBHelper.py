# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.Config import DBConf
import pymysql.cursors

class DBHelper:
    def __enter__( self ):
        try:
            self.connection = pymysql.connect( host = DBConf.IP, port = DBConf.PORT, 
                                                user = DBConf.User, password = DBConf.PassWord, 
                                                db = DBConf.DBName, charset = 'utf8mb4', 
                                                cursorclass = pymysql.cursors.DictCursor )
        except:
            self.connection = None
            raise RuntimeError( 'MySQL Connect Failed' )
            
        return self
                                            
    def __exit__( self, type, value, trace ):
        if self.connection:
            self.connection.close()
            
    def getRandomIP( self ):
        try :
            with self.connection.cursor() as cursor :
                cursor.execute( "SELECT * FROM `tblIPPool` AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM `tblIPPool`)-(SELECT MIN(id) FROM `tblIPPool`))+(SELECT MIN(id) FROM `tblIPPool`)) AS id) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id LIMIT 1" )
                data = cursor.fetchone()
                return data
        except:
            return None
            
    def getAllIP( self ):
        try :
            with self.connection.cursor() as cursor :
                cursor.execute( "SELECT * FROM `tblIPPool`" )
                data = cursor.fetchall()
                return data
        except:
            return None
        
    def delIP( self, hash ):
        try :
            with self.connection.cursor() as cursor :
                cursor.execute( 'delete from tblIPPool where hash = %s', hash )
            self.connection.commit()
        except:
            pass
        
    def addIP( self, ip, port, hash ):
        try :
            with self.connection.cursor() as cursor :
                cursor.execute( 'INSERT INTO tblIPPool ( `hash`, `ip`, `port` ) values( %s, %s, %s )', ( hash, ip, port ) )
            self.connection.commit()
        except:
            pass