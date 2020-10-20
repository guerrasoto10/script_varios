import platform
import socket
import distro
import pwd, grp
import subprocess

def firsty(): #mediante el uso de librerias obtenemos alguna información del equipo donde ejecutemos
    subprocess.run(['python3','./proces.py'])
    return

def second():
    subprocess.run(['sh','./proces.sh'])  #mediante el uso de bash obtenemos información complementaria del equipo donde ejecutemos
    return

def main():
    firsty()
    second()
    return
    
if __name__=='__main__':
       main()
      