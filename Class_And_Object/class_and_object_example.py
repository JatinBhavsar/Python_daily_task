class sample:
    # class variable
    a = 12
    b = 96

    # class methods
    def add(self):
        return self.a + self.b;

obj = sample()
print (obj.a)
print (obj.b)

print("Addition = ", obj.add())
