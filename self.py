import datetime

class Person():
	
	def __init__(self,name, surname, birthdate, address, telephone, email):
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.address = address
		self.telephone = telephone
		self.email = email
		
	def age(self):
		today = datetime.date.today()
		age = today.year-self.birthdate.year
		if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
			age -= 1
		return age
			
person = Person("Jane", "Doe", datetime.date(1992, 3,12), "No 12 short street, Greenville", "555 388, 2772", "jane.doe@example.com")

print(person.name)
print(person.email)
print(person.age())
		