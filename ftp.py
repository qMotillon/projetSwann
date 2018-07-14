import os
from os.path import basename
from ftplib import FTP

def etat():
    ftp = FTP('127.0.0.1', 'admin', 'root')
    print("Tu es connecte")
    etat = ftp.getwelcome()
    print("Etat du ftp: \n", etat)
    ftp.quit()

def copie():
    ftp = FTP('127.0.0.1', 'admin', 'root')
    print("On va copier un fichier dans le serveur ftp")
    list()
    search = input("Avant tout definis ton site afin de te faciliter dans ta recherche d'utilisateur\n").upper()
    fichier = input("Copie colle le chemin du fichier que tu veux copier\n")
    file = open(fichier, 'rb')
    ftp.storbinary('STOR ' + search + "/" + basename(fichier), file)
    file.close()
    print("Fichier copie dans", search)
    ftp.quit()

def checkdirect():
    ftp = FTP('127.0.0.1', 'admin', 'root')
    folderName = ['ftp_Lyon','ftp_Paris','ftp_Strasbourg','ftp_Nantes']
    i = 0
    for f in folderName:
        if f in ftp.nlst():
            continue
        else:
            ftp.mkd(f)
            print(f," created")



def list():
    ftp = FTP('127.0.0.1', 'admin', 'root')
    ftp.dir()
    ftp.quit()
