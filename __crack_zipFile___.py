#!/usr/bin/env python

import zipfile
import sys
from threading import Thread
import optparse

ok = False
def extractPass(zfil, passwd):
        try:
            zfil.extractall(pwd=passwd)
            print '[+] the Crack was Successfull. The Pass is: ' + str(passwd)
            ok=True
        except Exception, e:
            pass

def main():
    try:
        parser = optparse.OptionParser("usage" + " -f <zipfile.zip> -d <dictionnary>")
        parser.add_option('-f', dest='zname', type='string', help='specify zip file')
        parser.add_option('-d', dest='dname', type='string', help='specify a text file')
        (options, args)= parser.parse_args()
        if(options.zname == None) | (options.dname==None):
            print parser.usage
            exit(0)
        else:
            zname = options.zname
            dname = options.dname
        print '[+] Cracking Password of ' + zname
        zfile=zipfile.ZipFile(zname)
        passfile = open(dname, 'r')
        for lines in passfile:
            lines = lines.strip('\n')
            if ok == False:
                t = Thread(target=extractPass, args=(zfile, lines))
                t.start()
                t.join()
            else:
                exit(0)
    except Exception, e:
        print e
if __name__=='__main__':
    main()
        
