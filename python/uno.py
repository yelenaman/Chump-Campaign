import random

colors = ["blue", "red", "yellow", "pink"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9] * 2 + [0] + ["+2", "skip", "reverse"] * 2

#functions for card object
class Card(object):
    #defines card object
    def __init__(self, color, value):
        self.color = color
        self.value = value
    #card to string
    def __str__(self):
            return self.color + " " + str(self.value)

#defines player of this game
class Player(object):
    def __init__(self, name, type):
        self.name = name
        self.cards=[]
        self.type = type
        self.goes_first = False

    # returns list of cards which are valid to play
    def checkValid(self, prevCard):
        valid = []
        for x in range(len(self.cards)):
            if (self.cards[x] == 'wild' or self.cards[x] == 'superwild' or self.cards[x].color == prevCard.color
                or self.cards[x].value == prevCard.value):
                valid.append(x)
        return valid

#defines deck of cards to draw from
def create_deck():
    deck = []
    for x in colors:
        for y in values:
            deck.append(Card(x, y))
    deck += ["wild", "superwild"] * 4
    random.shuffle(deck)
    return deck

def printHand(player):
    print 'your cards are: '
    for x in range(len(human.cards)):
        print str(x) + ') ' + str(human.cards[x])
    # for x in pile:
    #     print x

#plays card, adds to pile, subtracts from hand
def playCard(player, num):
    pile.append(player.cards.pop(num))

#prepare players
CPU = Player('CHUMP THE CHIPMUNK', 'CPU')

print("This is Uno!")

#create human player
human = Player('name', 'human')
human.name = raw_input("what is your name? ")

#starts game
def game_start(players):
    deck = create_deck()
    playersHaveCards = True
    for player in players:
        for x in range(7):
            player.cards.append(deck.pop())
    return deck

#### PLAYS GAME
players = [human] + [CPU]
deck = game_start(players)
pile = []
pile.append(deck.pop())
print 'Get ready!'
playerStatement = ''
for x in range(len(players)):
    playerStatement += players[x].name
    if x != len(players)-1:
        playerStatement += " vs "
print playerStatement

printHand(players[0])

print 'The card at the top of the pile is:'
print pile[len(pile)-1]

first = random.randint(1,2)
if first == 1:
    turnOfHuman = True
else:
    turnOfHuman = False

playersHaveCards = True

#play of the game
while playersHaveCards:
    #handles the computer's turn if computer is first
    while not turnOfHuman:
        topOfPile = pile[len(pile)-1]
        valid = players[1].checkValid(topOfPile)
        while len(valid) == 0:
            players[1].cards.append(deck.pop())
            valid = players[1].checkValid(topOfPile)
        playCard(players[1], int(valid[random.randint(0, len(valid))-1]))
        topOfPile = pile[len(pile)-1]
        print "Chump played: " + str(topOfPile)
        if len(players[1].cards) == 0:
            playersHaveCards = False
            break;
        if topOfPile == 'wild' or topOfPile == 'superwild':
            if topOfPile == 'superwild':
                for x in range(4):
                    players[0].cards.append(deck.pop())
            color = colors[random.randint(0,3)]
            print 'color is now ' + color
            pile.append(Card(color, 'none'))
            topOfPile = pile[len(pile)-1]
        if topOfPile.value == '+2':
            for x in range(2):
                players[0].cards.append(deck.pop())
        if topOfPile.value != 'reverse' and topOfPile.value != 'skip':
            turnOfHuman = True
    #handles human's turn
    while turnOfHuman:
        topOfPile = pile[len(pile)-1]
        valid = players[0].checkValid(topOfPile)
        while len(valid) == 0:
            players[0].cards.append(deck.pop())
            valid = players[0].checkValid(topOfPile)
        #prompts user to choose which card to play
        printHand(players[0])
        print "choose number of card to play. Your choices are:"
        print valid
        #plays card picked by user
        playCard(players[0], int(raw_input()))
        topOfPile = pile[len(pile)-1]
        if len(players[0].cards) == 0:
            playersHaveCards = False
            break;
        #if user played wild card, handles the situation
        if topOfPile == 'wild' or topOfPile == 'superwild':
            if topOfPile == 'superwild':
                for x in range(4):
                    players[1].cards.append(deck.pop())
            for x in range(len(colors)):
                print str(x) + ") " + colors[x]
            color = colors[int(raw_input('choose a color (0, 1, 2, or 3)'))]
            print 'color is now ' + color
            pile.append(Card(color = color, value = 'none'))
            topOfPile = pile[len(pile)-1]
        #handles +2 cards
        if topOfPile.value == '+2':
            for x in range(2):
                players[1].cards.append(deck.pop())
        # if user played skip or reverse, handles the situation
        if topOfPile.value != 'reverse' and topOfPile.value != 'skip':
            turnOfHuman = False
        while not turnOfHuman:
            topOfPile = pile[len(pile)-1]
            valid = players[1].checkValid(topOfPile)
            while len(valid) == 0:
                players[1].cards.append(deck.pop())
                valid = players[1].checkValid(topOfPile)
            playCard(players[1], int(valid[random.randint(0, len(valid))-1]))
            if len(pile) >= 10:
                deck.append(pile.pop(0))
                random.shuffle(deck)
            topOfPile = pile[len(pile)-1]
            print "Chump played: " + str(topOfPile)
            if len(players[1].cards) == 0:
                playersHaveCards = False
                print 'chump won'
                break;
            if topOfPile == 'wild' or topOfPile == 'superwild':
                if topOfPile == 'superwild':
                    for x in range(4):
                        players[0].cards.append(deck.pop())
                color = colors[random.randint(0,3)]
                print 'color is now ' + color
                pile.append(Card(color = color, value = 'none'))
                topOfPile = pile[len(pile)-1]
            if topOfPile.value == '+2':
                for x in range(2):
                    players[0].cards.append(deck.pop())
            if topOfPile.value != 'reverse' and topOfPile.value != 'skip':
                turnOfHuman = True
if turnOfHuman:
    print 'Congratulations, you won!'
else:
    print 'BOOO you lose!'
