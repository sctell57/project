class Item:
	def __init__(self, name, id, price):
		self.__name = name
		self.__id = id
		self.__price = price
	def getName(self, name):
		return self.__name
	def getId(self, id):
		return self.__id
	def getPrice(self, price):
		return self.__price
	def __str__(self):
		return self.__name + ' ' + str(self.__id) + ' ' + self.__price
class Shipment():
	def __init__(self, shipid):
		self.shipid = str(shipid)
		self.items = []
	def getId(self):
		return self.shipid
	def getItems(self):
		return self.items
	def addItem(self, item):
		self.items.append(item)
	def __str__(self):
		result = self.shipid + ': ['
		if len(self.items) == 0:
			return result + ']'
		result += str(self.items[0])
		ctr = 1
		length = len(self.items)
		while ctr < length:
			result += ',' + str(self.items[ctr])
			ctr += 1
		return result + ']'
	def __repr__(self):
		return str(self)
    
class ItemException(Exception):
	def __init__(self, message):
		self.message = message
		self.items = []
    
	def __str__(self):
		return self.message
class PriceException(Exception):
	def __init__(self, message):
		self.message = message
		self.items = []
	def __str__(self):
		return self.message
    
def processFile(filename):
	file = open(filename, "r")
	contents = file.readlines()
	file.close()
	return contents
    
def main(file):
	shipments = []
	ctr = 0
	length = len(file)
	while ctr < length:
		line = file[ctr].rstrip()
		if line.isdigit():
			shipment = Shipment(line)
			shipments.append(shipment)
			ctr += 1
		elif ' ' in line:
			pieces = line.split(' ')
			name = pieces[0]
			itemid = pieces[1]
			price = file[ctr + 1].rstrip()
			if "$" not in price:
				raise PriceException('invalid item')
			if "-" in price:
				raise PriceException('invalid item')
			if price.count(".") == 2:
				raise PriceException('invalid item')
			decimal = price.split(".")[1]
			if len(decimal) > 2:
				raise PriceException('invalid item')
			item = Item(name, itemid, price)
		else:
			raise ItemException('invalid item')
	return shipments