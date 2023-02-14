class C :
    # class variable
    a = 12
    b = 96

    # class methods
    def add(self):
        return self.a + self.b;
    def multi(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def sub(self):
        return self.a - self.b

obj = C()
print(obj.a)
print(obj.b)
print("Addition: ", obj.add())

obj = C()
print(obj.a)
print(obj.b)
print("Multiplication: ", obj.multi())

obj = C()
print(obj.a)
print(obj.b)
print("Division: ", obj.div())

obj = C()
print(obj.a)
print(obj.b)
print("Subtraction : ", obj.sub())
        

