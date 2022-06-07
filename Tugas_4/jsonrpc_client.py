#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_client.py

import sys
from jsonrpclib import Server

def main():
    proxy = Server('http://localhost:7002')
    while True:
        msg = input(">  ")
        msgSplit=msg.split()
        if(msgSplit[0]=="ls"):
            print(proxy.ls(msg))

        elif(msgSplit[0]=="get"):
            print(proxy.get(msg))
        elif(msgSplit[0]=="count"):
            print(proxy.count(msg))
        elif(msgSplit[0]=="put"):
            print(proxy.put(msg))
        elif(msgSplit[0]=="quit"):
            print(proxy.quit())
            proxy('close')()
            return
        else:
            print("Invalid Command")
        
if __name__ == '__main__':
    main()