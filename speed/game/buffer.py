from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the players letters.

    Stereotype:
        Information Holder

    Attributes: 
        _word (string): The letters in the word so far.
    """
    def __init__(self):
        pass

    def add_letter(self, letter):
        pass

    def get_word(self):
        pass

    def reset(self):
        pass