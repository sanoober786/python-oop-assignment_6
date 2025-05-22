#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Object Created:", cls.count)

a = Counter
b = Counter
Counter.show_count()