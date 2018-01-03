# /usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import hashlib

class XiCiParser:
    
    @staticmethod
    def parseDocument( html ):
        bsObj = BeautifulSoup( html, 'lxml' )
        result = []
        for tbl in bsObj.find_all( 'table', {'id':'ip_list'} ):
            for tr in tbl.findAll( 'tr' ):
                tdList = []
                for td in tr.findAll( 'td' ):
                    tdList.append( td )
                if len( tdList ) > 0:
                    result.append( tdList )
        ret = []
        for item in result:
            item[1] = str( item[1] )[4:-5]
            item[2] = str( item[2] )[4:-5]
            item[5] = str( item[5] )[4:-5].upper()
            if len( item[5] ) > 0 and item[5] != 'HTTPS':
                ret.append( { 'SOURCE': 'XC', 'IP': item[1], 'PORT': item[2], 'TYPE': item[5], 'HASH': hashlib.md5( ('http://' + item[1] + ':' + item[2]).encode('utf-8') ).hexdigest() } )
        del result[ : ]
        return ret
        
class KuaiIPParser:

    @staticmethod
    def parseDocument( html ):
        bsObj = BeautifulSoup( html, 'lxml' )
        result = []
        for tbl in bsObj.find_all( 'table', class_ = 'table table-bordered table-striped' ):
            for tr in tbl.findAll( 'tr' ):
                tdList = []
                for td in tr.findAll( 'td' ):
                    tdList.append( re.findall( r'>(.*?)</td>', str( td ), re.I | re.M | re.S )[0] )
                if len( tdList ) > 0:
                    result.append( tdList )
        if len( result ) > 0:
            result = result[ 1: ]
        ret = []
        for item in result:
            item[3] = item[3].upper()
            if len( item[3] ) > 0 and item[3] != 'HTTPS':
                ret.append( { 'SOURCE': 'KUAI', 'IP': item[0], 'PORT': item[1], 'TYPE': item[3], 'HASH': hashlib.md5( ('http://' + item[0] + ':' + item[1]).encode('utf-8') ).hexdigest() } )
        del result[ : ]
        return ret
        
class IP181Parser:

    @staticmethod
    def parseDocument( html ):
        bsObj = BeautifulSoup( html, 'lxml' )
        result = []
        for tbl in bsObj.find_all( 'table', class_ = 'table table-hover panel-default panel ctable' ):
            for tr in tbl.findAll( 'tr' ):
                tdList = []
                for td in tr.findAll( 'td' ):
                    tdList.append( str( td )[4:-5].replace( '\r\n', '' ) )
                if len( tdList ) > 0:
                    result.append( tdList )
        if len( result ) > 0:
            result = result[ 1: ]
        ret = []
        for item in result:
            item[3] = item[3].upper()
            if len( item[3] ) > 0 and item[3] != 'HTTPS':
                ret.append( { 'SOURCE': '181', 'IP': item[0], 'PORT': item[1], 'TYPE': item[3], 'HASH': hashlib.md5( ('http://' + item[0] + ':' + item[1]).encode('utf-8') ).hexdigest() } )
        del result[ : ]
        return ret
        
class Data5UParser:

    @staticmethod
    def parseDocument( html ):
        bsObj = BeautifulSoup( html, 'lxml' )
        result = []
        for tbl in bsObj.find_all( 'div', class_ = 'wlist' ):
            for ul in tbl.findAll( 'ul', class_ = 'l2' ):
                ulList = []
                for li in ul.findAll( 'li' ):
                    ulList.append( re.findall( r'>(.*?)</li>', str( li ), re.I | re.M | re.S )[0] )
                if len( ulList ) > 0:
                    result.append( ulList )
        ret = []
        for item in result:
            try:
                item[3] = re.findall( r'>(.*?)</a>', str( item[3] ), re.I | re.M | re.S )[0].upper()
            except:
                item[3] = ''
            if len( item[3] ) > 0 and item[3] != 'HTTPS':
                ret.append( { 'SOURCE': '5U', 'IP': item[0], 'PORT': item[1], 'TYPE': item[3], 'HASH': hashlib.md5( ('http://' + item[0] + ':' + item[1]).encode('utf-8') ).hexdigest() } )
        del result[ : ]
        return ret
        
class IP138Parser:
    
    @staticmethod
    def parseDocument( html ):
        return re.findall( r'您的IP是：\[(.*?)\]', html, re.I | re.M | re.S )[0]