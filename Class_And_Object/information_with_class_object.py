class B:
    # class variable
    a = 'jatin'
    b = 'bhavsarjatin24@gmail.com'
    c = 'xyz'

    # class method
    def info(self):
        return self.a, self.b, self.c;
obj = B()
print(obj.a)
print(obj.b)
print(obj.c)
print("Information: ", obj.info())

    
