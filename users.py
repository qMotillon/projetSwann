import database
import hashlib
from hashlib import md5
class Users:
	id = 1;
	username = ""
	role=""
	passwordHash= ""
	mail = ""
	site = ""
	c = database.conn.cursor()
	def create_user(self):
		self.nom = input("Quel est son nom ?\n").upper()
		self.prenom = input("Quel est son prénom ?\n").upper()
		self.username = self.prenom[0] + self.nom
		self.passwordHash = input("Entre ton mdp\n")
		self.passwordHash = md5(self.passwordHash.encode('utf-8')).hexdigest()
		self.mail = input("Entre son mail lol \n").upper()
		self.site = int(input("Site 1: Paris, Site 2 : Nantes, Site 3 : Lyon, Site 4 : Strasbourg\n"))
		if(self.site == 1):
			self.site="PARIS"
		elif(self.site == 2):
			self.site="NANTES"
		elif(self.site == 3):
			self.site="LYON"
		else:
			self.site="STRASBOURG"
		self.role = input("Souhaitez vous que l'user soit un Admin? 1 = Oui, * = Non\n")
		if(self.role =="1"):
			self.role="admin"
		else:
			self.role="user"
		c = database.conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,role,nom,prenom,username,passwordHash,mail,site)")
		c.execute("INSERT INTO users(role,nom,prenom,username,passwordHash,mail,site) VALUES (?,?,?,?,?,?,?)",(self.role,self.nom,self.prenom,self.username,self.passwordHash,self.mail,self.site,))
		#c.execute("INSERT INTO users (id,nom,prenom,username,passwordHash,mail,site)")
		database.conn.commit()

	def login(self):
		print("____________________________________________\n")
		username = input("Entrez votre pseudo : \n").upper()
		password = input("Entre votre mdp : \n")
		password = md5(password.encode('utf-8')).hexdigest()
		c = database.conn.cursor()
		c.execute("SELECT * FROM users WHERE username=:pseudo",{"pseudo" : username})
		data = c.fetchone()
		if(data == None):
			print("Mauvais Username!\n")
			self.login()
		elif(data[1] != "admin"):
			print("Vous n'êtes pas admin")
		else:
			while(password != data[5]):
				print("Mauvais password\n")
				password = input("Entre votre mdp : \n")
				password = md5(password.encode('utf-8')).hexdigest()
			print("Connexion Réussi !!\n")
			self.id = data[0]
			self.role = data[1]
			self.prenom = data[2]
			self.nom = data[3]
			self.username = data[4]
			self.passwordHash = data[5]
			self.mail = data[6]
			self.site = data[7]

	def change_role(self):
		print("____________________________________________\n")
		username = input("Vous voulez changer le role de quel user ?(Rentrer username) \n").upper()
		c = database.conn.cursor()
		c.execute("SELECT id FROM users WHERE username=:pseudo",{"pseudo" : username})
		data = c.fetchone()
		if(data == None):
			print("Mauvais Username!\n")
			self.change_role()
		else:
			role = input("Souhaitez vous que l'user soit un Admin? 1 = Oui, * = Non\n")
			if (role == "1"):
				c.execute("UPDATE users SET role='admin' WHERE username=:pseudo", {"pseudo": username})
				database.conn.commit()
			else:
				c.execute("UPDATE users SET role='user' WHERE username=:pseudo", {"pseudo": username})
				database.conn.commit()

	def search_users(self):
		print("____________________________________________\n Vous pouvez rechercher un utilisateur par son username, ou son id, ou vous pouvez même rechercher tous les users d'un site.\n")
		search = input("Qui souhaitez vous chercher (id,username,site)\n").upper()
		c = database.conn.cursor()
		c.execute("SELECT * FROM users WHERE username=:search OR id=:search OR site=:search ",{"search" : search})
		data = c.fetchall()
		print(data)