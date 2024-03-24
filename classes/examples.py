
# python3 examples.py

from uuid import uuid4
import random

# Make a class for a card game
class Suit:

    # suits = "♣️ ♠️ ❤️ ♦️"
    suits = "♣️ ♠️ ❤️ ♦️".split()
    numbers_and_faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def create_deck(self):
        print("------ Creating a Deck ------")
        deck = [(s, nf) for s in self.suits for nf in self.numbers_and_faces]
        return deck


class Card(Suit):
    
    def shuffle_cards(self, deck):
        print("------ Shuffling of Cards ------")
        random.shuffle(deck)
        return deck

    def choose_card(self, deck):
        print("------ Choosing a card ------")
        if deck:
            return random.choice(deck)
        return f"No card found in the deck"
    
    # def serve_cards(self, deck, names):

   


class Person:

    user_id = ""
    cards = []

    def __init__(self, name) -> None:
        self.name = name
        self.user_id = uuid4()

    @classmethod
    def serve_cards(self, users, deck):
        end = 0
        for idx, user in enumerate(users):
            start = end
            end = 8*(idx+1)
            print(start, end)
            # print(user.user_id)
            # print(user.cards)
            user.cards = deck[start:end]

            



card = Card()

deck = card.create_deck()
# print(deck)

shuffled_deck = card.shuffle_cards(deck)
print(shuffled_deck)

card_chosen = card.choose_card(shuffled_deck)
print(card_chosen)
print(type(card_chosen))
print()
print(f"{card_chosen[1]} of {card_chosen[0]} was chosen")


print("Enter 4 users to play: ")
users = []
for _ in range(4):
    users.append(input())


user_instances = []

for username in users:
    u = Person(username)
    user_instances.append(u)

print(user_instances)
Person.serve_cards(user_instances, shuffled_deck)

for user in user_instances:
    print(f"Name: {user.name}")
    print(f"Name: {user.user_id}")
    print(f"Name: {user.cards}")






