class Pupil():
    def __init__(self ,name ,form):
        self.name = name
        self.form = form
    def __str__(self):
        return self.name + " " + self.form

pupils = []
pupils.append(Pupil("Harry", "8C"))
pupils.append(Pupil("Carol", "8A"))
pupils.append(Pupil("Gary", "8B"))
pupils.append(Pupil("Alice", "8B"))
pupils.append(Pupil("Daniel", "8D"))
pupils.append(Pupil("Eve", "8C"))
pupils.append(Pupil("Gary", "8C"))
pupils.append(Pupil("Bob", "8A"))
pupils.append(Pupil("Jeremy", "6X"))
pupils.append(Pupil("Callum", "6X"))

def bubbleSort(list1):
    while True:
        changed = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                changed = True
                temp = list1[i]
                list1[i] = list1[i + 1]
                list1[i + 1] = temp
        if changed == False:
            break
    return list1

formlist = []
for pupil in pupils:
    formlist.append(pupil.form)
formlist = bubbleSort(list(set(formlist)))

dict1 = {}
for form in formlist:
    dict1[form] = []

for pupil in pupils:
    dict1[pupil.form].append(pupil.name)

for form in dict1:
    peeps = bubbleSort(dict1[form])
    for name in peeps:
        print(name + " " + form)