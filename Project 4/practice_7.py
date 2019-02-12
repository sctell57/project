class Experience:
	def __init__(self, name, company, year):
		self.__name = name 
		self.__company = company
		self.__year = year
	#def getName(self):
		# return self.__name
	#def setName(self, name):
		#self.__name = name
	def __str__(self):
		return self.__name + ' ' + self.__company + ' ' + str(self.__year)
class Resume:
	def __init(self, name):
		self.__name = name
		self.__skills = []
	def addExperience(self, exp):
		self.__skills.append(exp)
	def __str__(self):
		result = self.__name + ' ['
		ctr = 0
		while ctr < len(self.__skills):
			result += str(self.__skills[ctr]) + ', '
			ctr += 1
		if len(self.__skills) == 0:
			return result + ' ]'
		result = result[:-2] 
		result += ']'
		return result
def load(lst):
	db = {}
	i = 0
	while i < len(lst):
		stuff = lst[i].split(',')
		name = stuff[1]
		year = stuff[2]
		if year not in db.keys():
			db[year] = [name]
		else:
			db[year] += [name]
		i += 1
	return db