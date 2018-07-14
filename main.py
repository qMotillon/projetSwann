import portscan
import bruteforce
import logs
from ftp import *
from users import Users
from mail_bombing import SMTP


user = Users()
smtp=SMTP()

def portscan_menu():
    choice = input("Press :\n1 to scan a range of ports\n2 to scan one port\n3 to cancel\n")
    if choice == "1":
        logs.writeInLogSimple(user.username," a lancé le scan d'une range de port")
        portscan.rangePorts()
        portscan_menu()
    elif choice == "2":
        logs.writeInLogSimple(user.username," a lancé le scan d'un port")
        portscan.onePort()
        portscan_menu()
    elif choice == "3":
        main_menu()
    else:
        print("Wrong key")
        portscan_menu()

def users_menu():
    choice = input("Press :\n1 to create a new user\n2 to search an user\n3 to edit or delete an user\n4 to cancel\n")
    if choice == "1":
        logs.writeInLogSimple(user.username," a lancé la création d'User")
        user.create_user()
        users_menu()
    elif choice == "2":
        logs.writeInLogSimple(user.username," a lancé la recherche d'User")
        user.show_all_users()
        user.search_users()
        users_menu()
    elif choice == "3":
        logs.writeInLogSimple(user.username," a lancé l'édition ou suppression d'User")
        user.show_all_users()
        user.edit_or_delete()
        users_menu()
    elif choice == "4":
        # return ou
        main_menu()
    else:
        print("Wrong key")
        users_menu()

def ftp_menu():
    choice = input("Press :\n1 pour Afficher le répertoire de travail actuel"
                   "\n2 Listez les dossiers du ftp"
                   "\n3 Etat du ftp"
                   "\n4 Pour Push un fichier"
                   "\n5 recup un audit ?"
                   "\n6 quitter\n")
    if choice == "1":
        whereami()
        ftp_menu()
    elif choice == "2":
        logs.writeInLogSimple(user.username, " a lancé le listage des dossiers")
        list()
        ftp_menu()
    elif choice == "3":
        logs.writeInLogSimple(user.username, " a demande l'etat du serveur ftp")
        etat()
        ftp_menu()
    elif choice == "4":
        logs.writeInLogSimple(user.username, " a lancé le push de fichier")
        copie()
        ftp_menu()
    elif choice == "5":
        logs.writeInLogSimple(user.username, " a lancé la recuperation du fichier d'audit")
        ftp_menu()
    elif choice == "6":
        return
    else:
        print("Wrong key")
        ftp_menu()


def main_menu():
    choice = input(
        "Press :\n1 to manage users\n2 to manage ftp\n3 to test brute force\n4 to scan ports\n5 to try the mail bombing\n6 to see the logs file\n7 to exit\n")
    if choice == "1":
        logs.writeInLogSimple(user.username," à lancer la gestion d'User")
        users_menu()
        main_menu()
    elif choice == "2":
        logs.writeInLogSimple(user.username," à lancer la gestion FTP")
        checkdirect()
        ftp_menu()
        main_menu()
    elif choice == "3":
        logs.writeInLogSimple(user.username," à lancer le bruteforce")
        bruteforce.bruteforce()
        main_menu()
    elif choice == "4":
        logs.writeInLogSimple(user.username," à lancer le scan de port")
        portscan_menu()
        main_menu()
    elif choice == "5":
        logs.writeInLogSimple(user.username," à lancer le mail bombing")
        smtp.lancement()
        main_menu()
    elif choice == "6":
        # logs()
        main_menu()
    elif choice == "7":
        exit()
    else:
        print("Wrong key")
        main_menu()

#user.login()
main_menu()
