class Team:
    # initialize team constructor
    def __init__(self, name, points, last5):
        self.name = name
        self.points = points
        self.last5 = last5

    # calc number of consecutive losses using last 5 matches
    def calcConsLosses(self):
        count = 0
        # initialize max
        result = 0
        for i in range(0, len(self.last5)):
            # Reset count when 0 is found
            if (self.last5[i] == 1):
                count = 0
            # If 1 is found, increment count
            # and update result if count
            # becomes more.
            else:
                # increase count
                count += 1
                result = max(result, count)
            self.losses = result
        return self.losses

    # display team details
    def __str__(self):
        return self.name + ' ' + str(self.points) + ' ' + str(self.last5)


class League:
    # initialize league constructor
    def __init__(self, teams):
        self.teams = teams

    # display league details
    def __str__(self):
        return str(self.teams)

    # get teams that have n consecutive losses
    def getTeamsWithNLosses(self, n):
        # initialize list to store teams
        result = []
        # iterate through teams
        for team in self.teams:
            # if team has n consecutive losses, add to list
            if (team.calcConsLosses() == n):
                result.append(team)
        return result


# create teams
GT = Team("GT", 20, [1, 1, 0, 0, 1])
LSG = Team("LSG", 18, [1, 0, 0, 1, 1])
RR = Team("RR", 16, [1, 0, 1, 0, 0])
DC = Team("DC", 14, [1, 1, 0, 1, 0])
RCB = Team("RCB", 14, [0, 1, 1, 0, 0])
KKR = Team("KKR", 12, [0, 1, 1, 0, 1])
PBKS = Team("PBKS", 12, [0, 1, 0, 1, 0])
SRH = Team("SRH", 12, [0, 0, 1, 0, 1])
CSK = Team("CSK", 8, [0, 0, 0, 0, 1])
MI = Team("MI", 6, [0, 0, 0, 1, 1])

# create list of teams
IPL = League([GT, LSG, RR, DC, RCB, KKR, PBKS, SRH, CSK, MI])

# print filtered teams based on n losses
n = int(input("Enter number of consecutive losses: "))

# store the filtered teams
resltingTeams = IPL.getTeamsWithNLosses(n)

# display the results
sumOfPoints = 0
for team in resltingTeams:
    sumOfPoints += team.points
    print(team)

print("Average points: ", sumOfPoints // len(resltingTeams))
