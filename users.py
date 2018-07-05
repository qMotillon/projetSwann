import database
import hashlib
class Users:
	id = 1;
	pseudo = "Gildarytzs"
	passwordHash= "password"
	mail = "test@test.com"
	site = "Nantes"

	def __init__(self,pseudo,password,mail,site):
		m = hashlib.md5()
		self.pseudo = pseudo
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
