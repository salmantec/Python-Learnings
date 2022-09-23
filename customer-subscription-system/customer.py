class Customer:
    def __init__(self, fname, lname, tier=('free', 0)):
        self.fname = fname
        self.lname = lname
        self._tier = tier[0]
        self._cost = tier[1]

    def bill_for(self, months):
        return months * self._cost

    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @classmethod
    def premium(cls, fname, lname):
        return cls(fname, lname, tier=('premium', 10))


user1 = Customer('Mohamed', 'Salman')

print('user1 full name', user1.name)

bills = user1.bill_for(2)
print('user1 bills', bills)
