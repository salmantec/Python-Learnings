class House:
	def __init__(self, size, rooms, baths):
		self.size = size
		self.rooms = rooms
		self.baths = baths

	@classmethod
	def create(cls, description):
		"""The description should be like `SIZE ROOMS BATHS`."""
		size, rooms, baths = description.split(' ')
		# Make a house using these
		return cls(float(size), int(rooms), int(baths))
	@staticmethod
	def build_door(width, height):
		return (width, height)

home = House.create("1000 2 2")


