# Jayson Yin
# 11/28/22
# Need to be able to 'Hit' and 'Stand'

import random

card_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_suits = ['diamonds', 'hearts', 'spades', 'clubs']
cards = []
for suit in card_suits:
    for number in card_numbers:
        card = (suit, number)
        cards.append(card)

# Will print the cards in the order that they are in the deck
def printCards():
    i = 1
    for card in cards:
        print(f"{i}: {card[1]} of {card[0]}")
        i += 1

# Will randomly swap cards throughout the deck
# The 'amount' parameter will dictate how many times it is shuffled
def shuffle(amount = 1):
    for i in range(amount):
        for j in range(len(cards)):
            random_int = random.randint(0, len(cards) - 1)
            temp = cards[j]
            cards[j] = cards[random_int]
            cards[random_int] = temp

def dealCards():
    for i in range(2):
        pulled_card = cards.pop()
        player_cards.append(pulled_card)
        pulled_cards.append(pulled_card)
        pulled_card = cards.pop()
        dealer_cards.append(pulled_card)
        pulled_cards.append(pulled_card)

player_cards = []
dealer_cards = []
pulled_cards = []

class Hand():

    def __init__(self, turn, cards):
        self.turn = turn
        self.cards = cards

    def showCards(self, type):
        if type == 'player':
            print('Player Hand:')
            for card in self.cards:
                print(f"\t{card[1]} of {card[0]}")
        if type == 'dealer':
            print('Dealer Hand:')
            print(f"\t{self.cards[0][1]} of {self.cards[0][0]}")
            print("\tUnknown card...")

    # All this does is check if the hand is a bust
    def checkBust(self):
        total = 0
        for card in self.cards:
            total += card[1]
        if total > 21:
            return True
        else:
            return False
    
    def checkValue(self):
        total = 0
        for card in self.cards:
            total += card[1]
        return total
    
    def checkBlackjack(self):
        if self.turn == 1 and self.checkValue() == 21:
            return True
        else: 
            return False
    
    def check(self):
        if self.checkBust() == True:
            return 'bust'
        if self.checkBlackjack() == True:
            return True

    def hit(self):
        pulled_card = cards.pop()
        player_cards.append(pulled_card)
        pulled_cards.append(pulled_card)
        self.turn += 1
        self.cards = player_cards

def runBlackjack():
    shuffle(15)
    dealCards()
    player_hand = Hand(1, player_cards)
    dealer_hand = Hand(1, dealer_cards)
    while True:
        player_hand.showCards('player')
        dealer_hand.showCards('dealer')
        if player_hand.checkBust() == True:
            break
        if player_hand.checkBlackjack() == True:
            break
        response = input("\nWould you like to 'hit' or 'stand': ")
        if response.lower() == 'hit':
            player_hand.hit()
        else:
            break
    player_hand.showCards('player')
    print('Dealer Hand:')
    for card in dealer_cards:
        print(f"\t{card[1]} of {card[0]}")
    if player_hand.checkBust() == True:
        print("\nYou have busted!")
        return 'loss'
    elif player_hand.checkBlackjack() == True:
        print("\nBlackjack!")
        return 'win'
    elif dealer_hand.checkBust() == True:
        print("\nThe dealer busted! You win!")
        return 'win'
    elif player_hand.checkValue() > dealer_hand.checkValue():
        print('\nYou have won!')
        return 'win'
    elif player_hand.checkValue() < dealer_hand.checkValue():  
        print("\nYou have lost!")
        return 'loss'

wins = 0
losses = 0

print('Welcome to Blackjack')
print('The objective is to be dealt a higher number than the dealer without going over 21')
print('Good luck!\n')
winloss = runBlackjack()
if winloss == 'win':
    wins += 1
else:
    losses += 1
while True:
    reponse = input("\nWould you like to play again? ('Y'/'N') ")
    player_cards = []
    dealer_cards = []
    for card in pulled_cards:
        popped_card = pulled_cards.pop()
        cards.insert(0, popped_card)
    if reponse.lower() == 'y':
        winloss = runBlackjack()
        if winloss == 'win':
            wins += 1
        else:
            losses += 1
    else:
        break
    

print("\nHere is your win/loss breakdown")
print(f"\tWins: {wins}")
print(f"\tLosses: {losses}")
print("\nThank you for using this Blackjack program.")





