import database
import logs
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
		nom = input("Quel est son nom ?\n").upper()
		prenom = input("Quel est son prénom ?\n").upper()
		username = prenom[0] + nom
		password_hash = input("Entre ton mdp\n")
		password_hash = md5(password_hash.encode('utf-8')).hexdigest()
		mail = input("Entre son mail lol \n").upper()
		if(self.role=="MASTER"):
			site = input("Toi Master peut decider a quel site affecter : 1/Paris  2/Lyon  3/Strasbourg  4/Nantes\n")
			if(site=="1"):
				site = "PARIS"
			elif(site=="2"):
				site = "LYON"
			elif (site == "3"):
				site = "STRASBOURG"
			else:
				site = "NANTES"
		else:
			print("Le site est automatiquement ajoute (PARIS,NANTES,LYON,STRASBOURG) et correspond au votre")
			if(self.site=="LYON"):
				site = "LYON"
			elif(self.site=="NANTES"):
				site="NANTES"
			elif (self.site == "PARIS"):
				site = "PARIS"
			elif (self.site == "STRASBOURG"):
				site = "STRASBOURG"
			print("Il a donc ete affecte au site :", site)

		role = input("Souhaitez vous que l'user soit un Admin? 1 = Oui, * = Non\n")
		if(role =="1"):
			role="ADMIN"
		else:
			role="USER"
		c = database.conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,role,nom,prenom,username,password_hash,mail,site)")
		c.execute("INSERT INTO users(role,nom,prenom,username,password_hash,mail,site) VALUES (?,?,?,?,?,?,?)", (role,nom,prenom,username,password_hash,mail,site,))
		#c.execute("INSERT INTO users (id,nom,prenom,username,password_hash,mail,site)")
		database.conn.commit()
		print("User/Admin created\n")
		logs.writeInLogDuo(self.username,username," à crée le user : ")

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
			if(data[1] != "ADMIN" and data[1] != "MASTER"):
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
			logs.writeInLogSimple(self.username," vient de se connecter")

	def edit_or_delete(self):
		print("____________________________________________\n")
		search = input("Quel user souhaitez vous modifier?(Rentrer username ou ID) \n").upper()
		c = database.conn.cursor()
		c.execute("SELECT * FROM users WHERE username=:search OR id=:search",{"search" : search})
		data = c.fetchone()
		while(data == None):
			print("Mauvais Username ou ID!\n")
			search = input("Vous voulez changer le role de quel user ?(Rentrer username) \n").upper()
			c.execute("SELECT * FROM users WHERE username=:search OR id=:search", {"search": search})
			data = c.fetchone()
		whatToEdit= input("Que souhaitez vous modifier ?\n 1- Role\n2- Nom\n3- Prenom\n4- Username\n 5- Password\n 6- Mail\n7- Site\n8- /!\ Suppression /!\ ").upper()
		if(whatToEdit == "1"):
			role = input("Souhaitez vous que l'user soit un Admin? 1 = Oui, * = Non\n")
			logs.writeInLogDuo(self.username,search," a moodifié le rôle de l'user : ")
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
				print(data[3])
				logs.writeInLogDuo(self.username, search," a modifié le nom et username de ")
				prenom = data[3]
				username = prenom[0] + newData
				c.execute("UPDATE users SET nom=:newData,username=:username  WHERE username=:search OR id=:search", {"search": search,"newData": newData,"username": username})
				database.conn.commit()
			else:
				logs.writeInLogDuo(self.username, search," a modifié le nom de ")
				c.execute("UPDATE users SET nom=:newData WHERE username=:search OR id=:search", {"search": search,"newData": newData})
				database.conn.commit()
		elif(whatToEdit == "3"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
			username=input("Souhaitez vous que l'username soit également changé?1 - Oui\n")
			if(username=="1"):
				logs.writeInLogDuo(self.username, search," a modifié le prénom et username de ")
				nom = data[2]
				username = newData[0] + nom
				c.execute("UPDATE users SET prenom=:newData,username=:username  WHERE username=:search OR id=:search", {"search": search,"newData": newData,"username": username})
				database.conn.commit()
			else:
				logs.writeInLogDuo(self.username, search," a modifié le prénom de ")
				c.execute("UPDATE users SET prenom=:newData WHERE username=:search OR id=:search", {"search": search,"newData": newData})
				database.conn.commit()
		elif(whatToEdit == "4"):
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
			logs.writeInLogDuo(self.username, search," a modifié le username de ")
			c.execute("UPDATE users SET username=:newData WHERE username=:search OR id=:search",{"search": search, "newData": newData})
			database.conn.commit()
		elif(whatToEdit == "5"):
			logs.writeInLogDuo(self.username, search," a modifié le mot de passe de ")
			newData=input("Quel nouvel valeur souhaitez vous?\n")
			newData = md5(newData.encode('utf-8')).hexdigest()
			c.execute("UPDATE users SET password_hash=:newData WHERE username=:search OR id=:search",{"search": search, "newData": newData})
			database.conn.commit()
		elif(whatToEdit == "6"):
			logs.writeInLogDuo(self.username, search," a modifié le mail de ")
			newData=input("Quel nouvel valeur souhaitez vous?\n").upper()
			c.execute("UPDATE users SET mail=:newData WHERE username=:search OR id=:search",{"search": search, "newData": newData})
			database.conn.commit()
		elif(whatToEdit == "7"):
			logs.writeInLogDuo(self.username, search," a modifié le site de ")
			newData = int(input("Site 1: Paris, Site 2 : Nantes, Site 3 : Lyon, Site 4 : Strasbourg\n"))
			if (newData == 1):
				c.execute("UPDATE users SET site='PARIS' WHERE username=:search OR id=:search",{"search": search})
				database.conn.commit()
			elif (newData == 2):
				c.execute("UPDATE users SET site='NANTES' WHERE username=:search OR id=:search",{"search": search})
				database.conn.commit()
			elif (newData == 3):
				c.execute("UPDATE users SET site='LYON' WHERE username=:search OR id=:search",{"search": search})
				database.conn.commit()
			else:
				c.execute("UPDATE users SET site='STRASBOURG' WHERE username=:search OR id=:search",{"search": search})
				database.conn.commit()
		elif (whatToEdit == "8"):
			logs.writeInLogDuo(self.username, search," a supprimé l'user : ")
			c.execute("DELETE FROM users WHERE username=:search OR id=:search", {"search": search})
			database.conn.commit()
		else:
			print("Erreur\n")

	def search_users(self):
		print("____________________________________________\n Vous pouvez rechercher un utilisateur par son username,nom/prenom, ou son id, ou vous pouvez même rechercher tous les users d'un site.\n")
		search = input("Qui souhaitez vous chercher (id,username,site)\n").upper()
		logs.writeInLogDuo(self.username, search, " a recherché : ")
		c = database.conn.cursor()
		c.execute("SELECT id,role,nom,prenom,username,mail,site FROM users WHERE username=:search OR id=:search OR site=:search OR nom=:search OR prenom=:search",{"search" : search})
		data = c.fetchall()
		#print(data)
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

	def show_all_users(self):
		print("Affichage")
		search = input("Avant tout definis ton site afin de te faciliter dans ta recherche d'utilisateur\n").upper()
		c = database.conn.cursor()
		c.execute("SELECT id,role,nom,prenom,username,mail,site FROM users WHERE site=:search", {"search": search})
		data = c.fetchall()
		print("Voici les utilisateur presents a ", search)
		# print(data)
		print("ID  Role  Nom  Prenom  Username  Mail  Site ")
		for i in range(0, len(data)):
			for j in range(0, len(data[0])):
				print(data[i][j], end="   ")
			print(" ")