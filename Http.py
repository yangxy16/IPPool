# /usr/bin/env python3
# -*- coding: utf-8 -*-

from Config import DBConf
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class WebRequestHandler( BaseHTTPRequestHandler ):    
      
    def do_GET( self ):  
        querypath = urlparse( self.path )
        filepath, query = querypath.path, querypath.query
        if not filepath.endswith( '/' ):
            filepath = filepath + '/'
        if filepath == '/' or filepath == '/getip/':
            self.send_response( 200 )
            self.end_headers()
            self.wfile.write( '114.114.114.114'.encode('utf-8') )
        elif filepath == '/getall/':
            self.send_response( 200 )
            self.end_headers()
            self.wfile.write( '114.114.114.114\r\n8.8.8.8'.encode('utf-8') )
        elif filepath == '/del/':
            id = query.split( '=' )[1]
            self.send_response( 200 )
            self.end_headers()
            self.wfile.write( id.encode('utf-8') )
        else:
            self.send_response( 404 )
            self.end_headers()
        
if __name__ == '__main__':  
    httpd = HTTPServer( ( '0.0.0.0', 8080 ), WebRequestHandler )
    httpd.serve_forever()  