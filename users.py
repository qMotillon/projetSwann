import database
import hashlib
from hashlib import md5
class Users:
	id = 1;
	pseudo = "Gildarytzs"
	passwordHash= "password"
	mail = "test@test.com"
	site = "Nantes"
	c = database.conn.cursor()
	def login(self):
		self.nom = input("Quel est son nom ?\n")
		self.prenom = input("Quel est son prénom ?\n")
		self.username = self.prenom[0] + self.nom
		self.passwordHash = input("Entre ton mdp\n")
		self.passwordHash = md5(self.passwordHash.encode('utf-8')).hexdigest()
		self.mail = input("Entre son mail lol \n")
		self.site = int(input("Site 1: Paris, Site 2 : Nantes, Site 3 : Lyon, Site 4 : Strasbourg\n"))
		if(self.site == 1):
			self.site="Paris"
		elif(self.site == 2):
			self.site="Nantes"
		elif(self.site == 3):
			self.site="Lyon"
		else:
			self.site="Strasbourg"
		print(self.pseudo)
		print(self.passwordHash)
		print(self.site)
		c = database.conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,nom,prenom,username,passwordHash,mail,site)")
		c.execute("INSERT INTO users(nom,prenom,username,passwordHash,mail,site) VALUES (?,?,?,?,?,?)",(self.nom,self.prenom,self.username,self.passwordHash,self.mail,self.site,))
		#c.execute("INSERT INTO users (id,nom,prenom,username,passwordHash,mail,site)")
		database.conn.commit()

	def __init__(self):
		print("____________________________________________\n")
		username = input("Entrez votre pseudo : \n")
		password = input("Entre votre mdp : \n")
		password = md5(password.encode('utf-8')).hexdigest()
		print(password+"\n")
		c = database.conn.cursor()
		c.execute("SELECT passwordHash FROM users WHERE username=:pseudo",{"pseudo" : username})
		passwordDB = c.fetchone()
		if(password == passwordDB[0]):
			print("Connexion Réussi !!\n")
			self.menu()
		else:
			print("U SUCKER\n")
			self.__init__();
