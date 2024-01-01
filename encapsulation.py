class computer:
    def __init__(self):
        self.__maxprice=100
    def display(self):
        print("max price:",self.__maxprice)
    def update(self,price):
        self.__maxprice=price

object1=computer()
object1.display()
object2=computer()
#object2.__maxprice=200 {__variable is private,so we can not change externally}
object2.update(200)
object2.display()

""" we can restrict access to methods and variables.
This prevents data from direct modification
which is called encapsulation"""
