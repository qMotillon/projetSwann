import database
import hashlib
class Users:
	id = 1;
	pseudo = "Gildarytzs"
	passwordHash= "password"
	mail = "test@test.com"
	site = "Nantes"

	def __init__(self,nom,prenom,password,mail,site):
		m = hashlib.md5()
		self.nom = nom
		self.prenom = prenom
		self.username = prenom[0] + nom
		self.passwordHash = m.update(password.encode('utf-8'))
		self.mail = mail
		if(site == 1):
			self.site="Paris"
		elif(site == 2):
			self.site="Nantes"
		elif(site == 3):
			self.site="Lyon"
		else:
			self.site="Strasbourg"
		print(self.pseudo)
		print(self.passwordHash)
		print(self.site)
		c = database.conn.cursor()
		c.execute("CREATE TABLE users (id INTEGER AUTO_INCREMENT,nom,prenom,username,passwordHash,mail,site)")
		c.execute("INSERT INTO users(nom,prenom,username,passwordHash,mail,site) VALUES (?,?,?,?,?,?)",(self.nom,self.prenom,self.username,self.passwordHash,self.mail,self.site,))
		#c.execute("INSERT INTO users (id,nom,prenom,username,passwordHash,mail,site)")
		database.conn.commit()
