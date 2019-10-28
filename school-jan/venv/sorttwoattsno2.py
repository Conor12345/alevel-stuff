class Pupil():
    def __init__(self ,name ,form):
        self.name = name
        self.form = form

pupils = []
pupils.append(Pupil("Harry", "8C"))
pupils.append(Pupil("Carol", "8A"))
pupils.append(Pupil("Gary", "8B"))
pupils.append(Pupil("Alice", "8B"))
pupils.append(Pupil("Daniel", "8D"))
pupils.append(Pupil("Eve", "8C"))
pupils.append(Pupil("Gary", "8C"))
pupils.append(Pupil("Bob", "8A"))

def printall():
    for i in pupils:
        print(i.name,i.form)

while True:
    changed = False
    for i in range(len(pupils) - 1):
        if pupils[i].form > pupils[i + 1].form:
            changed = True
            temp = pupils[i]
            pupils[i] = pupils[i + 1]
            pupils[i + 1] = temp
        elif pupils[i].form == pupils[i + 1].form:
            if pupils[i].name > pupils[i + 1].name:
                changed = True
                temp = pupils[i]
                pupils[i] = pupils[i + 1]
                pupils[i + 1] = temp
    if not changed:
        break

printall()