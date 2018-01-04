# /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    整个架构中，HTTP服务属于细枝末节的东西，所以简单实现了，通过ab做了简单的压测，对一般的分布式爬虫来说QPS够用了
'''

from Lib.DBHelper import DBHelper
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class WebRequestHandler( BaseHTTPRequestHandler ):    
      
    def do_GET( self ):  
        querypath = urlparse( self.path )
        filepath, query = querypath.path, querypath.query
        if not filepath.endswith( '/' ):
            filepath = filepath + '/'
        if filepath == '/getip/':
            with DBHelper() as db:
                ip = db.getRandomIP()
                if ip:
                    self.send_response( 200 )
                    self.end_headers()
                    self.wfile.write( json.dumps( { 'IP' : ip['ip'], 'PORT' : str( ip['port'] ), 'HASH' : ip['hash'] }, ensure_ascii = False ).encode( 'utf-8' ) )
                else:
                    self.send_response( 404 )
                    self.end_headers()
        elif filepath == '/delip/':
            hash = query.split( '=' )[1]
            if hash and len( hash ) == 32:
                with DBHelper() as db:
                    db.delIPByHash( hash )
                self.send_response( 200 )
                self.end_headers()
            else:
                self.send_response( 404 )
                self.end_headers()
        else:
            self.send_response( 404 )
            self.end_headers()
        
class HttpWrapper:

    def __init__( self ):
        httpd = HTTPServer( ( '0.0.0.0', 8080 ), WebRequestHandler )
        try:
            httpd.serve_forever()
        except:
            raise SystemExit( 'HTTP Server Stopped' )