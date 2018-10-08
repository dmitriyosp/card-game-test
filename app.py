from enum import Enum
from enum import IntEnum
from random import *


full_deck = []
partial_deck =[]
player1_cards = []
player2_cards = []
player3_cards = []

#Название карты
class Card(IntEnum):
    ШЕСТЬ = 6
    СЕМЬ = 7
    ВОСЕМЬ = 8
    ДЕВЯТЬ = 9
    ДЕСЯТЬ = 10
    ВАЛЕТ = 11
    ДАМА = 12
    КОРОЛЬ = 13
    ТУЗ = 14

# Карточная масть
class Suit(Enum):
    ПИКА = 'пика'
    КРЕСТА = 'креста'
    ЧИРВА = 'чирва'
    БУБНА = 'бубна'

plr_quant = input("Введите колличество игроков: ")

#Класс для хранения информации об игральных картах
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit


#функция для работы с коллодой карт
def create_deck():
    for suit in Suit :
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck


                

#Взятие одной случайной карты из коллоды
def draw_card(deck):
    rand_card = randint(0, len(deck) - 1)
    return deck.pop(rand_card)

def give_card():
    count=0
    while(len(partial_deck) > 0 ):
        count=count+1
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))
        player3_cards.append(draw_card(partial_deck))
        if count==6: break

print(plr_quant)

create_deck()  #создание коллоды карт

shuffle(full_deck) #перетасовка коллоды

partial_deck = list(full_deck)

give_card()   #раздача карт игрокам

for i in range(0, 6):
    print("Player 1   Card:  ", player1_cards[i].card, " Suit: ",player1_cards[i].suit)

print()

for i in range(0, 6):
    print("Player 2   Card:  ", player2_cards[i].card, " Suit: ",player2_cards[i].suit)

print()

for i in range(0, 6):
    print("Player 3   Card:  ", player3_cards[i].card, " Suit: ",player3_cards[i].suit)