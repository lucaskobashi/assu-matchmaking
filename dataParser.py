from person import Person

file = open('test.csv', "r")
entries = [line.rstrip() for line in file][1:]

allPeople = []

# populated all entries
for i in entries:
    allPeople.append(Person(i))

