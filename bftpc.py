#   Better FTP Client
#
#   bftpc.py
#   version: 1.0
#   for updates check:  github.com/jet/bftpc/README.md
#

from ftplib import FTP
import getpass
import os

bftpcversion = '1.0'
print('bftpc')

hostname = input('hostname: ')
userLogin = input('login: ')
password = getpass.getpass('password: ')


def grabfile(filename):
    ftp = FTP(hostname)
    ftp.login(userLogin, password)
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()


def placefile(filename):
    ftp = FTP(hostname)
    ftp.login(userLogin, password)
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()


def upload(nameoffile):
    ftp = FTP(hostname)
    ftp.login(userLogin, password)
    ftp.encoding = 'utf-8'

    with open(nameoffile, "rb") as file:
        ftp.storbinary(f"STOR {nameoffile}", file)

    ftp.dir()
    print('\nYou uploaded file: ' + nameoffile + '\n')

    session(hostname, userLogin, password)


def session(ip, user, passwd):
    ftp = FTP(ip)
    ftp.login(user, passwd)
    while True:
        command = input('[' + os.getcwd() + ']' + '&[' + ftp.pwd() + ']: ')
        splittedCommand = command.split(' ')

        if command == 'list':
            ftp.retrlines('LIST')
        if command == 'logout':
            ftp.quit()
            break
        if command == 'clear':
            try:
                os.system('clear')
            except:
                print('that is not linux')
        if command == 'cls':
            try:
                os.system('cls')
            except:
                print('that is not windows')
        if splittedCommand[0] == 'cwd':
            towhere = splittedCommand[1]
            ftp.cwd(towhere)
        if command == 'pwd':
            print(ftp.pwd())
        if splittedCommand[0] == 'rmd':
            rmdname = splittedCommand[1]
            ftp.rmd(rmdname)
        if splittedCommand[0] == 'mkd':
            mkdname = splittedCommand[1]
            ftp.mkd(mkdname)
        if splittedCommand[0] == 'del':
            delname = splittedCommand[1]
            ftp.delete(delname)
        if splittedCommand[0] == 'fjet':
            if splittedCommand[1] == 'download':
                grabfile(splittedCommand[2])
                placefile(splittedCommand[2])
            if splittedCommand[1] == 'upload':
                fileapellido = splittedCommand[2]
                ftp.quit()
                upload(fileapellido)
        if splittedCommand[0] == 'cld':
            os.chdir(splittedCommand[1])
        if splittedCommand[0] == 'csd':
            ftp.cwd(splittedCommand[1])
        if command == 'ver':
            print('\nbftpc version: ' + bftpcversion)


session(hostname, userLogin, password)


#   official open-source simple ftp client of the jet framework
#   available on all platforms that support python
