class MotorVehicle:
	def __init__(self, range):
		self.range = range
		self.tank = range

	def travel(self, distance):
		if distance > self.tank:
			print("Not enough in the tank. Only traveled {self.tank} KM.")
			self.tank = 0
		else:
			print(f"VOOOM! Traveled {distance} KM.")
			self.tank -= self.distance

	def refuel(self):
		print("Refueling...")
		self.tank = self.range
	
	def __str__(self):
		return f"Vehicle(range={self.range}, tank={self.tank})"

mv = MotorVehicle(100)

print(mv)

mv.travel(50)

mv.travel(30)

mv.travel(30)

print(mv)

mv.refuel()

print(mv)
