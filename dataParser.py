from person import Person

file = open('test.csv', "r")
entries = [line.rstrip() for line in file][1:]

allPeople = []

# populated all entries
for i in entries:
    allPeople.append(Person(i))

findBoo = True


def perfectMatch(source, potential):

    # sexuality
    sexualities = source.checkSexuality()
    psexualities = potential.checkSexuality()

    if potential.gender not in sexualities:
        return 0
    elif source.gender not in psexualities:
        return 0

    # # hair
    # if source.hairPreference != 8:  # source has preference
    #     if source.hairPreference != potential.hair:
    #         return 0

    # height
    # if source.heightPreference != 5:
    #     if source.heightPreference != potential.height:
    #         return 0

    # chose school
    # if source.choseSchool != potential.choseSchool:
    #     return 0

    # find location
    # if source.findLive != 0:
    #
    #     if source.findLive == 1:  # find on campus
    #         if potential.live == 0:  # they are off campus
    #             return 0
    #
    #     elif source.findLive == 2:  # find off campus
    #         if potential.live == 1:  # they are on campus
    #             return 0

    # profanity
    # if source.findBadWords == 0 and potential.badWords > 0:
    #     return 0

    # problem
    # if source.problem != potential.problem:
    #     return 0

    # music
    # if source.music != potential.music:
    #     return 0

    # age preference
    if source.agePreference != "doesn't matter":

        if source.agePreference == "older":
            if potential.age < source.age + 3:
                return 0

        elif source.agePreference == "same age and older":
            if potential.age < source.age:
                return 0

        elif source.agePreference == "same age and younger":
            if potential.age > source.age:
                return 0

        elif source.agePreference == "same age only":
            if potential.age != source.age:
                return 0

    # about them
    # if source.aboutThem != "doesn't matter":
    #     if source.aboutThem != potential.aboutYou:
    #         return 0

    return 1


def likeUBack(source, potential):
    if source in potential.potentialPeople:
        return True
    return False

if findBoo:
    for person in allPeople:
        for target in allPeople:
            if person == target:
                continue
            elif perfectMatch(person, target) == 1:
                person.potentialPeople.append(target)



for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        if not likeUBack(i, j):
            i.removePotential(j)

for i in allPeople:
    for j in i.potentialPeople:
        print(i.name + " is matched with " + j.name)