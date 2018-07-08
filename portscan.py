import socket
import subprocess
import sys
from datetime import datetime

def portScanning():
    server= input("Quel est l'ip du server que vous souhaitez scanner?")
    server= socket.gethostbyname(server)
    print("Scanning ports inc ^^")
    startScan = datetime.now()
    try:
        for port in range(0,1025):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((server,port))
            if result == 0:
                print(" Port {}: Open".format(port))
            else:
                print(" Port {}: Closed".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Vous avez annulé le scan")
        sys.exit()
    except socket.gaierror:
        print('Mauvaise ip')
        sys.exit()
    except socket.error:
        print("Impossible de se co au server")
        sys.exit()
    endScan = datetime.now()
    total = endScan - startScan
    print("Scan complété en :",total)