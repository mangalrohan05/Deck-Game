import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

value = {'Two':2, 'Three':3, 'Four': 4, 'Five': 5, 'Six':6, 'Seven': 7, 'Eight':8, 
         'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13 ,'Ace':14}


class Deck:

    def __init__(self):
        self.card_set = []

        for suit in suits:
            for rank in ranks:
                set_card = Cards(suit, rank)

                self.card_set.append(set_card)
    
    def shuffle(self):
        random.shuffle(self.card_set)

    def throw_card(self):
        return self.card_set.pop()

class Cards:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank

        self.value = value[self.rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove(self):
        return self.cards.pop(0)

    def add(self, new_card):

        if type(new_card) == type([]):
            self.cards.extend(new_card)
        else:
            self.cards.append(new_card)

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards'
    
new_deck = Deck()
new_deck.shuffle() #shuffled deck created

p1 = Player('one')
p2 = Player('two') #players created

for i in range(26):
    p1.add(new_deck.throw_card())
    p2.add(new_deck.throw_card())

game_on =  True

count = 0

while(game_on):

    count += 1
    print(f'Round {count}')


    if len(p1.cards) == 0:
        print('P2 Wins!')
        game_on = False
        break

    if len(p2.cards) == 0:
        print('P1 Wins!')
        game_on = False
        break
    
    p1_cards = []
    p1_cards.append(p1.remove())

    p2_cards = []
    p2_cards.append(p2.remove())

    at_war = True

    print(f'p1 throw: {p1.cards[0]}, p2 throw: {p2.cards[0]}')
    
    print(f'p1 has {len(p1.cards)-1} cards, p2 has {len(p2.cards)-1} cards')

    while(at_war):

        if p1_cards[-1].value > p2_cards[-1].value:
            p1.add(p1_cards)
            p1.add(p2_cards)
            at_war = False

        elif p1_cards[-1].value < p2_cards[-1].value:
            p2.add(p2_cards)
            p2.add(p1_cards)
            at_war = False


        else:
            print('War!')

            if len(p1.cards) < 5:
                print('P2 Wins!')
                game_on = False
                break
    
            elif len(p2.cards) < 5:
                print('P1 Wins!')
                game_on = False
                break
                
            else:
                for num in range(5):
                    p1_cards.append(p1.remove())
                    p2_cards.append(p2.remove())
            