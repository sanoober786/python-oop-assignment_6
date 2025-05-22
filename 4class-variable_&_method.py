# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Old Bank"
   
    @classmethod
    def change_bank_name(cls , name):
        cls.bank_name = name

a = Bank()
b = Bank()
print(a.bank_name)

Bank.change_bank_name("New Bank")
print(b.bank_name)
