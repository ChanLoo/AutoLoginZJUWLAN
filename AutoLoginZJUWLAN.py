#coding:utf-8
'''
author: ChanLo
e-mail: chanlo@protonmail.ch
'''

import urllib
from urllib.request import urlopen, Request, URLError, HTTPError
from termcolor import colored, cprint  

username = '******'
password = '******'

data = {'action':'login','username':username,'password':password,'ac_id':'3','user_ip':'','nas_ip':'','user_mac':'','save_me':'1','ajax':'1'}
data = urllib.parse.urlencode(data)
try:
    req = Request('https://net.zju.edu.cn/srun_portal_pc.php?url=&ac_id=3')
    response = urlopen(req, data, timeout=10)
    content = response.read()
    response.close()
except URLError as e:
    if hasattr(e, 'reason'):
        info = '[ERROR] Failed to reach the server.\Reason: ' + str(e.reason)
    elif hasattr(e, 'code'):
        info = '[ERROR] The server couldn\'t fullfill the request.\nError code: ' + str(e.reason)
    else:
        info = '[ERROR] Unknown URLError'
        print(info)
except:
    import traceback
    print('Generic exception: ' + traceback.format_exc())
        