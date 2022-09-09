# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:21:37 2022

@author: mahak
"""
import random

def pick_a_card():
    card_suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    card_ranks = [2,3,4,5,6,7,8,9,10,'j','q','k','a']
    random_suits  = random.choice(card_suits)
    random_ranks = random.choice(card_ranks)
    print(f"The {random_ranks} of {random_suits}")

pick_a_card()