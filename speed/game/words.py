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
    # Vanessa
    def __init__(self):
         """The class constructor.
        
        Args:
            self (words): An instance of words.
        """
         super().__init__()
         self._words = words
         self._points = points
         self._prepare_list()
        

    
    def get_all(self):
        """Gets all the words from the list of words the player can try to type. 
        
        Args:
            self (words): instances of words
        returns:
            list of words to be typed
        """
        return self._words
        

    # Shane
    def move_word(self, word, x, y):
        # direction equal to x,y using the Point class
        # word = self._words[word]
        # word.set_velocity equal to direction
        # word.move_next()
        pass

    # Larry
    def word_check(self, word):
        # loop through the range of words
            # set text equal to self._words at current index
            # if text.get_text() is equal to word
                # call the set points function and pass the current word
                # set the current word to a new random word
                # return points
        # return 0
        pass

    def _add_word(self, text, position, velocity):
        """
        Adds a new word to the words list using the passed in text, position and velocity.

        Args:
            self (Words): an instance of words
            text (string) the words text.
            position (Point): The word's position.
            velocity (Point): The word's velocity.
        """
        word = Actor()
        word.set_text(text)
        word.set_position(position)
        word.set_velocity(velocity)
        self._words.append(word)
        

    # Larry
    def _prepare_list(self):
        """Prepares the word list by adding words from the library constant words.txt.
        
        Args:
            self (Words): an instance of Words.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(random.choice(constants.SNAKE_LENGTH)):
            text = n
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)

    # Josh
    def _set_points(self, word):
        # set _points equal to the length of word
        pass