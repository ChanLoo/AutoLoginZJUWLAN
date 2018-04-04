#coding:utf-8
'''
author: ChanLo
e-mail: chanlo@protonmail.ch
------------------
Describtion:
This is a module used to encrypt or decrypt the password.
'''

class Crypto(object):
    def __init__(self):
        pass

    def encrypt(self, key):
        pass

    def decrypt(self, key):
        pass
    
    def generate_key():
        import uuid
        import sys
        from binascii import unhexlify as unhex

        if sys.platform == 'win32':
            mac = _ipconfig_getnode()
        else:
            mac = _ifconfig_getnode()
        if mac == None:
            mac = hex(_random_getnode())[2:-1]
        ud = uuid.uuid1()
        ud = ud.hex
        hi_time = up[12:16]
        key = hi_time + mac
        return unhex(key)
        

if __name__ == '__main__':
    crypto = Crypto()
