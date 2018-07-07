import database
import hashlib
from hashlib import md5
class Users:
	id = 1;
	username = ""
	role=""
	password_hash= ""
	mail = ""
	site = ""
	c = database.conn.cursor()
	def create_user(self):
		self.nom = input("Quel est son nom ?\n").upper()
		self.prenom = input("Quel est son prénom ?\n").upper()
		self.username = self.prenom[0] + self.nom
		self.password_hash = input("Entre ton mdp\n")
		self.password_hash = md5(self.password_hash.encode('utf-8')).hexdigest()
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
			self.role="ADMIN"
		else:
			self.role="USER"
		c = database.conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,role,nom,prenom,username,password_hash,mail,site)")
		c.execute("INSERT INTO users(role,nom,prenom,username,password_hash,mail,site) VALUES (?,?,?,?,?,?,?)", (self.role, self.nom, self.prenom, self.username, self.password_hash, self.mail, self.site,))
		#c.execute("INSERT INTO users (id,nom,prenom,username,password_hash,mail,site)")
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
		else:
			while(password != data[5]):
				print("Mauvais password\n")
				password = input("Entre votre mdp : \n")
				password = md5(password.encode('utf-8')).hexdigest()
			if(data[1] != "ADMIN"):
				print("Vous n'êtes pas admin")
				self.login()
			print("Connexion Réussi !!\n")
			self.id = data[0]
			self.role = data[1]
			self.prenom = data[2]
			self.nom = data[3]
			self.username = data[4]
			self.password_hash = data[5]
			self.mail = data[6]
			self.site = data[7]

	def edit_or_delete(self):
		print("____________________________________________\n")
		search = input("Quel user souhaitez vous modifier?(Rentrer username ou ID) \n").upper()
		c = database.conn.cursor()
		c.execute("SELECT * FROM users WHERE username=:search OR id=:search",{"search" : search})
		data = c.fetchone()
		while(data == None):
			print("Mauvais Username!\n")
			username = input("Vous voulez changer le role de quel user ?(Rentrer username) \n").upper()
			c.execute("SELECT * FROM users WHERE username=:search OR id=:search", {"search": search})
			data = c.fetchone()
		whatToEdit= input("Que souhaitez vous modifier ?\n 1- Role\n2- Nom\n3- Prenom\n4- Username\n 5- Password\n 6- Mail\n7- Site\n8- /!\ Suppression /!\ ").upper()
		if(whatToEdit == "1"):
			role = input("Souhaitez vous que l'user soit un Admin? 1 = Oui, * = Non\n")
			if (role == "1"):
				c.execute("UPDATE users SET role='ADMIN' WHERE username=:search OR id=:search", {"search": search})
				database.conn.commit()
			else:
				c.execute("UPDATE users SET role='USER' WHERE username=:search OR id=:search", {"search": search})
				database.conn.commit()
		elif(whatToEdit == "2"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
			username=input("Souhaitez vous que l'username soit également changé?1 - Oui\n")
			if(username=="1"):
				prenom = data[3]
				username = prenom[0] + newData
				c.execute("UPDATE users SET nom=:newData AND username=:username  WHERE username=:search OR id=:search", {"search": search,"newData": newData,"username": username})
				database.conn.commit()
			else:
				c.execute("UPDATE users SET nom=:newData WHERE username=:search OR id=:search", {"search": search,"newData": newData})
				database.conn.commit()
		elif(whatToEdit == "3"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
			username=input("Souhaitez vous que l'username soit également changé?1 - Oui\n")
			if(username=="1"):
				nom = data[2]
				username = newData[0] + nom
				c.execute("UPDATE users SET prenom=:newData AND username=:username  WHERE username=:search OR id=:search", {"search": search,"newData": newData,"username": username})
				database.conn.commit()
			else:
				c.execute("UPDATE users SET prenom=:newData WHERE username=:search OR id=:search", {"search": search,"newData": newData})
				database.conn.commit()
		elif(whatToEdit == "4"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
		elif(whatToEdit == "5"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
		elif(whatToEdit == "6"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
		elif(whatToEdit == "7"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
		elif (whatToEdit == "8"):
			print("hello")
		else:
			print("Erreur\n")

	def search_users(self):
		print("____________________________________________\n Vous pouvez rechercher un utilisateur par son username,nom/prenom, ou son id, ou vous pouvez même rechercher tous les users d'un site.\n")
		search = input("Qui souhaitez vous chercher (id,username,site)\n").upper()
		c = database.conn.cursor()
		c.execute("SELECT id,role,nom,prenom,username,mail,site FROM users WHERE username=:search OR id=:search OR site=:search OR nom=:search OR prenom=:search",{"search" : search})
		data = c.fetchall()
		print(data)
		while(data==[]):
			print("Mauvaise recherche")
			search = input("Qui souhaitez vous chercher (id,username,site)\n").upper()
			c.execute("SELECT id,role,nom,prenom,username,mail,site FROM users WHERE username=:search OR id=:search OR site=:search OR nom=:search OR prenom=:search",{"search" : search})
			data = c.fetchall()
		print("ID  Role  Nom  Prenom  Username  Mail  Site ")
		for i in range(0, len(data)):
			for j in range(0, len(data[0])):
				print(data[i][j],end="   ")
			print("\n")