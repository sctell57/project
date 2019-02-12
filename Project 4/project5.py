class Item():
	def  __init__(self, name, id, price):
		self.name = name
		self.id = id
		self.price = price
        
	def getName(self):
		return self.name
	def getId(self):
		return self.id
	def getPrice(self):
		return self.price
        
	def __str__(self):
		return str(self.name) + " " + str(self.id) + " " + str(self.price)
class Shipment():
	def __init__(self, shipid):
		self.shipid = str(shipid)
		self.items = []
	def getId(self):
		return self.shipid
	def getItems(self):
		return self.items
	def addItem(self, item):
		self.items.append(str(item))
		self.items.sort(reverse = True)
	def __str__(self):
		result = self.shipid + ': ['
		if len(self.items) == 0:
			return result + ']'
		result += str(self.items[0])
		ctr = 1
		while ctr < len(self.items):
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
    
def main(l, integers):
	list1 = l
	shipments = []
	ctr = 0
	while ctr < len(list1):
		line = list1[ctr].rstrip('\n')
		if line.isdigit():
			ship_obj = Shipment(int(line))
			shipments.append(ship_obj)
			ctr += 1
		elif ' ' in line:
			pieces = line.split(' ')
			name = pieces[0]
			itemid = pieces[1]
			price = list1[ctr + 1].rstrip('\n')
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
			ship_obj.addItem(item)
			ctr += 2
		else:
			raise ItemException('invalid item')
		"""duplicate = false
	iterate through shipment.items()
		if shipmentItemID = newItemID
			duplicate = true
	if duplicate is not true:
		add new Item"""
	
	return shipments