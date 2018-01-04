# /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    import win32con, win32file, pywintypes
elif os.name == 'posix':
    import fcntl
            
class AutoLock:

    def __init__( self, mutexname ):
        self.filepath = mutexname + '.lock'
        self.f = None
    
    def __enter__( self ):
        try:
            self.f = open( self.filepath, 'wb' )
        except:
            raise RuntimeError( "File Path Error" )
            
        if os.name == 'nt':
            __overlapped = pywintypes.OVERLAPPED()
            hfile = win32file._get_osfhandle( self.f.fileno() )
            win32file.LockFileEx( hfile, win32con.LOCKFILE_EXCLUSIVE_LOCK, 0, 0xffff0000, __overlapped )
        elif os.name == 'posix':
            fcntl.flock( f.fileno(), fcntl.LOCK_EX )
        return self

    def __exit__( self, type, value, trace ):
        if self.f:
            if os.name == 'nt':
                __overlapped = pywintypes.OVERLAPPED()
                hfile = win32file._get_osfhandle( self.f.fileno() )
                win32file.UnlockFileEx( hfile, 0, 0xffff0000, __overlapped )
            elif os.name == 'posix':
                fcntl.flock( self.file.fileno(), fcntl.LOCK_UN )
            self.f.close()
            try:
                os.remove( self.filepath )
            except:
                pass