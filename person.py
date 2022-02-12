class Person:
    '''
    Class representation for a person that filled the ASSU Matchmaking service
    '''

    def __init__(self, line):

        # lines have the following info, separated by commas:
        '''

        :param line:
        [0] Timestamp
        [1] I have read and I accept the terms and conditions above
        [2] Gender Identity
        [3] Sexual Orientation
        [4] Year of study
        [5] NSID
        [6] Full name
        [7] How old are you?
        [8] Student Number
        [9] Major
        [10] What age do you prefer to hang with?
        [11] Your current hair colour is
        [12] Standing up straight you're	tall
        [13] What hair colour do you like on others ?
        [14] What height do you prefer ?
        [15] I chose this school because of the
        [16] I plan to stay in school until
        [17] Are you a student from
        [18] I live
        [19] I would like to meet someone who lives
        [20] What's your take on bad words? (i.e. profanity)
        [21] How do you tolerate profanity?
        [22] The best thing you have going is
        [23] What do you look for first in others?
        [24] I do most of my shopping
        [25] I am fully vaccinated
        [26] My monthly cell phone bill is
        [27] In a crowd you stand out because you're	Body piercing is
        [28] Most of my tunes are
        [29] I spend most of my time on my phone using
        [30] A first date should be
        [31] What do you do most when not in school?
        [32] The biggest problem facing today's generation is (besides COVID-19)
        [33] My ideal location is
        [34] Phone number (only digits)
        [35] What are you looking for?
        '''

        # holds Person objects
        self.potentialPeople = []
        self.name = None
        self.studentNumber = None
        self.nsid = None
        self.lookingFor = None
        self.sexuality = None
        self.age = None
        self.dataParser(line)

    def dataParser(self, line):
        '''
        Parses each line to populate a person object
        :param line:
        :return:
        '''
        items = line.split(',')
        self.name = items[6]
        """
        self.studentNumber = [8]
        self.nsid = [5]
        self.lookingFor = [35]
        self.sexuality = [
        
        """
        return 0

    def checkSexuality(self, sexuality):
        if sexuality == "Straight":
            return True
        return False
