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
        """The class constructor for buffer. Using the superclass constructor, initializes word set to blank, the position and updates the text
        """

        super().__init__()
        # add all attributes
        self._word = " "
        # set the position equal to 1, MAX_Y using the Point class
        position = Point(1, constants.MAX_Y)
        # self.set_postion(postion)
        self.set_position(position)
        # self.set_text(as demonstarted in requirements)
        self.set_text(f"Buffer: {self._word}")

    # Vanessa
    def add_letter(self, letter):
        """Adds the given letter to the word and sets the buffer text with the word and letter.
        
        Args:
            self (set_text): An instance of word.
            letter (letter): An instance of letter
        """
        word = self._word + letter
        self.set_text(f"Buffer: {word}")

        

    # Shane
    def get_word(self):
        
        return 

    # Josh
    def reset(self):
        """Resets the word to an empty string when called.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        self._word = ""