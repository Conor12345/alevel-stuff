class Person():

    def setName(self, first, second):
        self.firstName = first
        self.surname = second

    def getName(self):
        return self.firstName + " " + self.surname


class Teacher(Person):

    def setName(self, first, second):
        self.title = input("What is this teacher's tite? ")
        super().setName(first, second)

    def getName(self):
        return self.firstName + " " + self.surname

    def getFormalName(self):
        return self.title + " " + self.surname

    def setDepartment(self, d):
        self.department = d

    def getDepartment(self):
        return self.department


class Student(Person):

    def setForm(self, f):
        self.form = f

    def getForm(self, ):
        return self.form

    def __str__(self):
        return "A Student Called: " + self.getName()

p = Person()
p.setName("Conor", "Nichols")
print(p.getName())

t = Teacher()
t.setName("Aloha", "Mcdonald")
print(t.getName())
print(t.getFormalName())
t.setDepartment("Music")
print(t.getDepartment())

s = Student()
s.setName("David", "Daniels")
print(s.getName())
s.setForm("Mr Mcdonald")
print(s.getForm())
print(s)