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

        Args:
            self is an instance of Buffer
        """

        super().__init__()
        self._word = ""
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")

    
    def add_letter(self, letter):
        """Adds the given letter to the buffer and sets the buffer text with the word and letter.
        
        Args:
            self (set_text): An instance of buffer.
            letter (letter): An instance of letter
        """
        self._word += letter
        self.set_text(f"Buffer: {self._word}")

        

    # Shane
    def get_word(self):
        """Gets the word(s)
        
        Args:
            self (Buffer): An instance of Buffer."""
        
        return self._word

    # Josh
    def reset(self):
        """Resets the word to an empty string when called.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        self._word = ""