
class Person:
    def __init__(self, name, age, address): #constructor 
        self.name = name
        self.age = age
        self.address = address

    def eat(self): #self implies object
        print("Eat.")

    def walk(self):
        print("Walk.")

    def run(self):
        print("Run.")

class Male(Person): #Male inheriting Person.
    def eat(self):
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is eating.")

    def walk(self):
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is walking.")

    def run(self):
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is running.")
class Female(Person):
    def eat(self):
        super().eat() #super() le garda parent class ko eat() call hunxa.
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is eating.")

    def walk(self):
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is walking.")

    def run(self):
        print (self.name , "who is" ,self.age , "years old and lives in", self.address, "is running.")


ram = Male ( name = "Ram" , age = 27 , address = "Ayodhya") #ram is object of Male.
sita = Female ( name = "Sita", age = 25, address = "Janakpur")
ram.eat()
ram.walk()
ram.run()
sita.eat()
sita.walk()
sita.run()



