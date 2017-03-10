import random

class Card(object):

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def show(self):
        if self.value == 1:
            val = 'Ace'
        elif self.value == 13:
            val = 'King'
        elif self.value == 12:
            val = 'Queen'
        elif self.value == 11:
                val = 'Jack'
        print '{} or {}'.format(self.val, self.suit)
        # print str(self.val) + " of " + self.suit

# newCard=Card(7, "hearts")
# print newCard
# This gives us an object
# We can print newcard.val to get the value


class Deck(object):'''doest take anything'''
    def __init__(self):
        self.cards = []
        self.build()'''this is a method hence the ()'''

    def build(self):
        suits = ["Spades","Hearts","Diamonds","Club"]
        for x in range(1, 14):
            for y in range(len(suits)):
                newCards = Card(x,suits[y])
                self.cards.append(newCards)
        # return cards
# newDeck = Deck()
# for item in newDeck.cards:
#     item.show()


# fisher yates shuffle
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            # python tuples swap
            randi = random.randint(0,i)
            if i == randi:
                continue
            self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]


# Can also use random.shuffle function


class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def deal(self):
        return self.cards pop()

    def draw(self,deck, num=1): '''need something to draw from so we use deck'''
    for i in range (num):
        self.hand.append(deck.deal())




        # print (random.choice(deck))
    #
    def showHand(self):
        for card in self.hand
        card.show()
