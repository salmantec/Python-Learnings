class House:
	PER_SQUARE = 2.5
	def __init__(self, size, baths, rooms):
		self.size = size
		self.baths = baths
		self.rooms = rooms
	@property
	def price(self):
		return self.size * self.PER_SQUARE
	@price.setter
	def price(self, new_price):
		self.size =  new_price / self.PER_SQUARE

home = House(1000, 2, 2)

print('Size', home.size)
print('Rooms', home.rooms)
print('Baths', home.baths)

print('Price', home.price)

newPrice = home.price = 800
print('New-Price', newPrice)
