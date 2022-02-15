class Person:
    '''
    Class representation for a person that filled the ASSU Matchmaking service
    '''

    def __init__(self, line):

        # lines have the following info, separated by commas:
        '''

        :param line:
        [0] Option: 0 = boo, 1 = friend
        [1] Student number
        [2] Name
        [3] Age
        [4] NSID
        [5] Major
        [6] Phone
        [7] Gender
        [8] Sexual Orientation
        [9] Year
        [10] Age preference
        [11] Hair colour
        [12] Hair preference
        [13] Height
        [14] Height preference
        [15] I chose this school because
        [16] I plan to stay in school until
        [17] Student from
        [18] I live
        [19] I would like to meet someone who lives
        [20] What's your take on bad words? (i.e. profanity)
        [21] How do you tolerate profanity?
        [22] The best thing you have going is
        [23] What do you look for first in others?
        [24] I do most of my shopping
        [25] My monthly cell phone bill is
        [26] In a crowd you stand out because you're
        [27] Body piercing is
        [28] Most of my tunes are
        [29] I spend most of my time on my phone using
        [30] A first date should be
        [31] What do you do most when not in school?
        [32] The biggest problem facing today's generation is (besides COVID-19)
        [33] My ideal location is
        '''

        # holds Person objects
        self.potentialPeople = []

        self.option = None
        self.studentNumber = None
        self.name = None
        self.age = None
        self.nsid = None
        self.major = None
        self.year = None
        self.agePreference = None
        self.choseSchool = None
        self.planSchool = None
        self.studentFrom = None
        self.live = None
        self.findLive = None
        self.badWords = None
        self.findBadWords = None
        self.aboutYou = None
        self.aboutThem = None
        self.shopping = None
        self.phoneBill = None
        self.standOut = None
        self.music = None
        self.phoneTime = None
        self.activities = None
        self.problem = None
        self.location = None

        self.gender = None
        self.orientation = None
        self.hair = None
        self.hairPreference = None
        self.height = None
        self.heightPreference = None
        self.bodyPiercing = None
        self.datePreference = None

        self.dataParser(line)

    def dataParser(self, line):
        '''
        Parses each line to populate a person object
        :param line:
        :return:
        '''
        items = line.split(',')

        self.option = int(items[0])
        self.studentNumber = int(items[1])
        self.name = items[2]
        self.age = int(items[3])
        self.nsid = items[4]
        self.major = items[5]
        self.year = items[9]
        self.agePreference = items[10]
        self.choseSchool = int(items[15])
        self.planSchool = items[16]
        self.studentFrom = items[17]
        self.live = int(items[18])
        self.findLive = int(items[19])
        self.badWords = int(items[20])
        self.findBadWords = int(items[21])
        self.aboutYou = items[22]
        self.aboutThem = items[23]
        self.shopping = int(items[24])
        self.phoneBill = items[25]
        self.standOut = int(items[26])
        self.music = items[28]
        self.phoneTime = int(items[29])
        self.activities = int(items[31])
        self.problem = int(items[32])
        self.location = int(items[33])

        if self.option == 1:
            self.booPreferences(items)

        return 0

    def booPreferences(self, items):

        self.gender = items[7]
        self.orientation = items[8]
        self.hair = int(items[11])
        self.hairPreference = int(items[12])
        self.height = int(items[13])
        self.heightPreference = int(items[14])
        self.bodyPiercing = items[27]
        self.datePreference = items[30]

        return 0

    def checkSexuality(self):

        possibleGenders = []

        if self.orientation == "Straight":
            if self.gender == "Man":
                possibleGenders.append("Woman")
            elif self.gender == "Woman":
                possibleGenders.append("Man")

        elif self.orientation == "Gay":
            possibleGenders.append("Man")

        elif self.orientation == "Lesbian":
            possibleGenders.append("Woman")

        else:
            possibleGenders.append("Woman")
            possibleGenders.append("Man")

        return possibleGenders

    def removePotential(self, person):
        if person in self.potentialPeople:
            self.potentialPeople.remove(person)
        return 0