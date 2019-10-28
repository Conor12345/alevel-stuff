class Person():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def speak(self):
        print("Hello, my name is", self.getfullname() + "!")

    def getfullname(self):
        return self.firstname + " " + self.surname

    def kiss(self, otherperson):
        print(self.firstname , "kisses", otherperson.firstname)

p1 = Person("Andrew", "Anderson")
p2 = Person("Billy", "Bobson")
p3 = Person("David", "Davidson")

p1.kiss(p2)