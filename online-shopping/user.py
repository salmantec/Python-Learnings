from review import Review
from product import Product

class User:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.reviews = []

	def write_review(self, content, product):
			review = Review(content, self, product)
			self.reviews.append(review)
			product.reviews.append(review)

	def sell_product(self, name, description, price):
		product = Product(name, description, price, self, available=True)
		print(f"{product} is on the market!")

	def buy_product(self, product):
		if product.available:
			print(f"{self} is buying {product}")
			product.available = False
		else:
			print(f"{product} is no longer available.")

	def __str__(self):
		return f"User(id={self.id}, name={self.name})"