from random import shuffle
import random

class Deck():
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    def __init__(self):
        self.cards = []
        for suit in self.SUITE:
            for rank in self.RANKS:
                self.cards.append(f'{rank} of {suit}')
    def shuffle(self):
        random.shuffle(self.cards)

    def split_deck(self):
        self.half1=self.cards[1::2]
        self.half2=self.cards[0::2]
class Player:
    def __init__(self, name, hand):

        self.name = name
        self.hand=hand
    def play(self):
        playing_cards=[]
        playing_cards=self.hand.half[0]
        print('Player '+self.name+' put card '+playing_cards)
        self.hand.half.pop(0)
        return playing_cards
    def check_cards(self):
        if len(self.hand.half)>0:
            print('You can continue playing')
            return 0
        if len(self.hand.half) == 52:
            print(self.name + ', you win game')
            return 1
        if len(self.hand.half) == 0:
            print(self.name + ', you lost game')
            return 1

class Hand():
    def __init__(self, half):
        self.half = half

    def add_cards(self, playing_cards):
        self.half.append(playing_cards)
    def remove_cards(self,playing_cards):
        self.half.remove(playing_cards)






print("Welcome to War, let's begin...")

new_deck = Deck()
new_deck.shuffle()
print("Shuffle cards")
new_deck.split_deck()
hand1=Hand(new_deck.half1)
hand2=Hand(new_deck.half2)
player1=Player('Johnny Depp', hand1 )
player2=Player('Amber Heard', hand2 )
print('Wellcome '+player1.name+" and "+ player2.name+ " to the Game!")
rangs = [
        ['2 of H', '2 of D', '2 of S', '2 of C'],
        ['3 of H', '3 of D', '3 of S', '3 of C'],
        ['4 of H', '4 of D', '4 of S', '4 of C'],
        ['5 of H', '5 of D', '5 of S', '5 of C'],
        ['6 of H', '6 of D', '6 of S', '6 of C'],
        ['7 of H', '7 of D', '7 of S', '7 of C'],
        ['8 of H', '8 of D', '8 of S', '8 of C'],
        ['9 of H', '9 of D', '9 of S', '9 of C'],
        ['10 of H', '10 of D', '10 of S', '10 of C'],
        ['J of H', 'J of D', 'J of S', 'J of C'],
        ['Q of H', 'Q of D', 'Q of S', 'Q of C'],
        ['K of H', 'K of D', 'K of S', 'K of C'],
        ['A of H', 'A of D', 'A of S', 'A of C']

    ]





def find_card_index(card, rangs):
    for i, row in enumerate(rangs):
        if card in row:
            return i
    return -1  # Card not found


count = 0
contro_cards=list()
while count == 0:

    player1_card = player1.play()
    player2_card = player2.play()

    index_p1 = find_card_index(player1_card, rangs)
    index_p2 = find_card_index(player2_card, rangs)

    print(f"Index of {player1_card}: {index_p1}")
    print(f"Index of {player2_card}: {index_p2}")

    if find_card_index(player1_card, rangs) > find_card_index(player2_card, rangs):

        print(player1.name + " win")
        if len(contro_cards)>0:
            player1.hand.half.extend(contro_cards)
            contro_cards = []
        player1.hand.add_cards(player2_card)
        player1.hand.add_cards(player1_card)


    if find_card_index(player1_card, rangs) < find_card_index(player2_card, rangs):
        print(player2.name + " win")
        if len(contro_cards) > 0:
            random.shuffle(contro_cards)
            player2.hand.half.extend(contro_cards)
            contro_cards = []
        player2.hand.add_cards(player2_card)
        player2.hand.add_cards(player1_card)


    if find_card_index(player1_card, rangs) == find_card_index(player2_card, rangs):
        print(player1_card + " and " + player2_card + " have same rang")
        print(player1.name + " and " + player2.name + "have same rang")
        contro_cards.append(player1_card)
        contro_cards.append(player2_card)
        contro_cards.append(player1.play())
        contro_cards.append(player2.play())
        print(contro_cards)




    print(player1.hand.half)
    print(player2.hand.half)
    count = player1.check_cards()



