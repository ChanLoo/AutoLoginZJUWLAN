#coding:utf-8
'''
author: ChanLo
e-mail: chanlo@protonmail.ch
'''
import Detection
import DataSave
import urllib
from urllib.request import urlopen, Request, URLError, HTTPError
from termcolor import colored, cprint  

name_DB = 'UserDB'
use_account = 0
is_use_existing_account = True
aim_id = 1

def if_use_existing_account():
    while(use_account != 'Y' and use_account !='N'):
        use_account = input('Use existing account? (Y/N)\n')
        if use_account == 'Y':
            return True
        else use_account == 'N':
            return False

def get_user_UP():
    username = input('User name: ')
    password = input('Password: ')
    return username, password

def main():
    print('Hi, there.\n')
    UPSave = DataSave.UPSave()
    if not if_use_existing_account():
        username, password = get_user_UP()
        UPSave.create_DB(name_DB)
        UPSave.insert_to_DB(name_DB, username, password)
    else:
        username, password = UPSave.select_DB(name_DB, aim_id)
    data = {'action':'login','username':username,'password':password,'ac_id':'3','user_ip':'','nas_ip':'','user_mac':'','save_me':'1','ajax':'1'}
    data = urllib.parse.urlencode(data)
    try:
        req = Request('https://net.zju.edu.cn/srun_portal_pc.php?url=&ac_id=3')
        with urlopen(req, data.encode('utf-8'), timeout=10) as response:
            content = response.read()
            cprint('Checking network status...', 'green')
            detection = Detection.Detection()
            if detection.is_connected():
                print('Login Successfully!')
            else:
                print('Connection fail.')

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
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        cprint('/n[INFO] PROGRAM EXIT.', 'green')
