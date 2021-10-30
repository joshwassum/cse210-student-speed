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
    
    def __init__(self):
         """The class constructor.
        
        Args:
            self (words): An instance of words.
        """
         super().__init__()
         self._words = []
         self._points = 0
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
        direction = Point(x, y)
        # direction equal to x,y using the Point class
        word = self._words[word]
        # word = self._words[word]
        word.set_velocity(direction)
        # word.set_velocity equal to direction
        word.move_next()
        # word.move_next()

    # Larry
    def word_check(self, word):
        '''Checks the users typed input with the word list. Gets 

        Args:
            self (words): an instance of Words.
            text (string) the words text.

        '''        
        for i in range(0, len(self._words)):
            text = self._words[i]

            if text.get_text() == word:
                self._set_points(word)
                self._words[i].set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY))])
                return self._points
            
        return 0


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
        for i in range(constants.STARTING_WORDS):
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2 - 2)
            text = constants.LIBRARY[random.randint(0, len(constants.LIBRARY))]
            position = Point(x, y - i)
            velocity = Point(1, 0)

            self._add_word(text, position, velocity)

    # Josh
    def _set_points(self, word):
        """Sets _points equal to the length of word.

        Args:
            self (Words): an instance of Words.
            word (string): the word to check the length of.
        """
        self._points = len(word)
