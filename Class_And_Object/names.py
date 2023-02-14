class sample:
    def __init__(self,a):
        self.value = a
        
    def display(self) :
        print("Name: ", self.value)
        
name = input ("Enter YOur Name: ")
age = sample(name)
age.display()
