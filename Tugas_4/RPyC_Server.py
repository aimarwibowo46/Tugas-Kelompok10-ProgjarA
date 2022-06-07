#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_server.py

import rpyc
import os, glob, shutil

def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_ls(self, path):
        if len(path) == 1:
            mainPath = '*'
        else:
            mainPath = path[1]
        files = glob.glob(mainPath, recursive=True)
        basenames = ""
        for file in files:
            basenames += os.path.basename(file) + '\n'
        return basenames

    def exposed_get(self, path):
        pesan = " ".join(path[1:-1])
        pesanGet = pesan + '/' + path[-1]

        f = open(pesanGet, "rb")
        b = f.read()
        f.close()
        shutil.copy(pesanGet, r'client')

        results = "fetch: {} size: {} lokal: {}".format(pesan, len(b), path[-1])
        return results
    
    def exposed_count(self, path):
        if len(path) == 1:
            mainPath = '*'
        else:
            mainPath = path[1]
        listFile=glob.glob(mainPath)
        results = len(listFile)
        return results
    
    def exposed_put(self, data, path):
        shutil.copy(data, path)
        return "put {} lokasi: {}".format(data, path)

    def exposed_quit(self):
        return "quit"


if __name__ == '__main__':
    main()