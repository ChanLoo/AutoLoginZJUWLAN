#coding:utf-8
'''
author: ChanLo
e-mail: chanlo@protonmail.ch
------------------
Describtion:
This is a module used to check some functions whether is regular/
'''
import urllib
from urllib.request import urlopen, Request, URLError, HTTPError

class Detection(object):
    def __init__(self):
        self.test_url = 'http://cn.bing.com'

    def is_connected(self):
        '''
        Detect whether the connection is connected.
        '''
        req = Request(self.test_url)
        try:
            with urlopen(req, timeout=10) as response:
                content = response.read()
                resUrl = response.geturl()
                code = response.getcode()
        except URLError as e:
            return False
        
        if code == 200 and 'net.zju.edu.cn' not in content.decode():
            return True
        else:
            return False

    def wlan_available(self, wlan_name):
        pass

    def wlan_connected(wlan_name):
        pass

if __name__ == '__main__':
    detecttion = Detection()
    if detecttion.is_connected():
        print('Connection is established.')
    else:
        print('Connection fail.')

