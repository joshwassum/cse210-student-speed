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
    # Brian
    def __init__(self):
        # you need to call the superclass init function
        # add all attributes
        # set the position equal to 1, MAX_Y using the Point class
        # self.set_postion(postion)
        # self.set_text(as demonstarted in requirements)
        pass

    # Vanessa
    def add_letter(self, letter):
        # set word equal to word + letter
        # reset self.set_text(as demonstarted in requirements)
        pass

    # Shane
    def get_word(self):
        # return the word
        pass

    # Josh
    def reset(self):
        # set word equal to an empty string
        pass