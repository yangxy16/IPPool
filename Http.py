# /usr/bin/env python3
# -*- coding: utf-8 -*-

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
            self.send_response( 200 )
            self.end_headers()
            self.wfile.write( '114.114.114.114'.encode('utf-8') )
        else:
            self.send_response( 404 )
            self.end_headers()
        
if __name__ == '__main__':

    httpd = HTTPServer( ( '0.0.0.0', 8080 ), WebRequestHandler )
    try:
        httpd.serve_forever()
    except:
        pass