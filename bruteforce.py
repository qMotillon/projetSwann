import database
import hashlib
from hashlib import md5

def bruteforce():
    username = input("Entrez votre pseudo : \n").upper()
    your_list = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    complete_list = []
    password = ""
    passwordHash = ""
    c = database.conn.cursor()
    c.execute("SELECT * FROM users WHERE username=:pseudo", {"pseudo": username})
    data = c.fetchone()
    if (data == None):
        print("Mauvais Username!\n")
        bruteforce()
    else:
        while (passwordHash != data[5]):
            for current in range(10):
                a = [i for i in your_list]
                for y in range(current):
                    a = [x + i for i in your_list for x in a]
                    for j in range(len(a)):
                        password = a[j]
                        passwordHash = md5(password.encode('utf-8')).hexdigest()
                        #print("For l et ",password)
                        if(passwordHash == data[5]):
                            print("Le password est " + password)
                            return
                    #print("For y et ", password)
                #print("For current et ", password)
                complete_list = complete_list + a
        print("Le password est "+ password)
