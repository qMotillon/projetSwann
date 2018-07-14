import datetime
def writeInLogSimple(user,text):
    fichier = open("log.txt", "a")
    date = datetime.datetime.now()
    fichier.write("\n["+str(date.day)+"/"+str(date.month)+"/"+str(date.year)+"  "+str(date.hour)+":"+str(date.minute)+":"+str(date.second)+"] "+user+text)
    fichier.close()

def writeInLogDuo(user,target,text):
    fichier = open("log.txt", "a")
    date = datetime.datetime.now()
    fichier.write("\n["+str(date.day)+"/"+str(date.month)+"/"+str(date.year)+"  "+str(date.hour)+":"+str(date.minute)+":"+str(date.second)+"] "+user+text+target)
    fichier.close()
