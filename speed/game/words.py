from game import constants
from game.actor import Actor
from game.point import Point
import random

class Words(Actor):

    """A list of many actors creating a list of words. Facilitates the points per word, 
    and the generation of new words.

    Stereotypes:
        Information Holder

    Attributes:
        _words (list): a list to contain all of our instances of word actors.
        _points (int): keeping track of points in a given word.
    """

    def get_all(self):
        pass

    def move_word(self, word, x, y):
        pass

    def word_check(self, word):
        pass

    def _add_word(self, text, position, velocity):
        pass

    def _prepare_list(self):
        pass

    def _set_points(self, word):
        pass