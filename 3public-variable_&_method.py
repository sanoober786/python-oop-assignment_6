#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). 
#Instantiate the class and access both from outside the class.

class Car:
    def __init__(self , brand):
        self.brand = brand

    def Start(self):
        print(f"{self.brand} is starting...")

c1 = Car("Toyota")
print(c1.brand)
c1.Start()