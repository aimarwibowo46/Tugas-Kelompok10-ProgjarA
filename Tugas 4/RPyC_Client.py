#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc

def main():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    while True:
        msg = input(">  ")
        msgSplit=msg.split()
        if(msgSplit[0]=="ls"):
            print(proxy.root.ls(msgSplit))

        elif(msgSplit[0]=="get"):

            print(proxy.root.get(msgSplit))
        elif(msgSplit[0]=="count"):
            print(proxy.root.count(msgSplit))
        elif(msgSplit[0]=="put"):
            print(proxy.root.put(msgSplit[1], msgSplit[2]))
        elif(msgSplit[0]=="quit"):
            print(proxy.root.quit())
            proxy.close()
            return
        else:
            print("Invalid Command")

def noisy(string):
    print('Noisy:', repr(string))

if __name__ == '__main__':
    main()