import socket
import sys
from datetime import datetime

def rangePorts():
    server= input("Quel est l'ip du server que vous souhaitez scanner?")
    server= socket.gethostbyname(server)
    a,b = -1,-1
    while(a<0):
        a = int(input("A quel port souhaitez vous commencer?"))
    while(b<0):
        b = int(input("A quel port souhaitez vous arrêter ?"))
    if(a > b):
        c=b
        b=a
        a=c
    print("Scanning ports inc ^^")
    startScan = datetime.now()
    try:
        for port in range(a,b):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((server,port))
            if result == 0:
                print(" Port {}: Open".format(port))
            else:
                print(" Port {}: Closed".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Vous avez annulé le scan")
        return
    except socket.gaierror:
        print('Mauvaise ip')
        return
    except socket.error:
        print("Impossible de se co au server")
        return
    endScan = datetime.now()
    total = endScan - startScan
    print("Scan complété en :",total)

def onePort():
    server= input("Quel est l'ip du server que vous souhaitez scanner?")
    server= socket.gethostbyname(server)
    port=-1
    while(port<0):
        port = int(input("Quel port souhaitez vous scanner?"))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((server, port))
        if result == 0:
            print(" Port {}: Open".format(port))
        else:
            print(" Port {}: Closed".format(port))
        sock.close()

    except KeyboardInterrupt:
        print("Vous avez annulé le scan")
        return
    except socket.gaierror:
        print('Mauvaise ip')
        return
    except socket.error:
        print("Impossible de se co au server")
        return
