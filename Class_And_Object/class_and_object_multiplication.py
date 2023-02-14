class sample :
    #class variable
    a = 12
    b = 90
     #class methods
    def multi(self):
     return self.a * self.b;

obj = sample()
print(obj.a)
print(obj.b)
print("Multiplication , " , obj.multi())
