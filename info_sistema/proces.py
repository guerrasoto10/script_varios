import platform
import socket
import distro
import pwd, grp
import subprocess

def first(): #informacion varia del equipo usando diversas librerias de python
    print('System :', platform.system())
    print('O/S Version:', distro.linux_distribution())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print ('IP Adress:', (s.getsockname()[0]))
    s.close()
    print('Hostname:', platform.node())
    print ('Local Groups:')
    groups=[]
    for p in pwd.getpwall():
        a= grp.getgrgid(p[3])[0]
        if a not in groups:
            groups.append(a)
    print(sorted(groups))
    print ('Local Users (System and Regular):')
    users=[]
    for i in pwd.getpwall():
        a= i[0]
        if a not in users:
            users.append(a)
    print(sorted(users))
    return

first()