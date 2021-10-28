from time import sleep
from game import constants
from game.buffer import Buffer
from game.score import Score
from game.words import Words
import random

class Director:
    '''A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        _buffer (Buffer): an instance of Buffer.
        _input_service (InputService): The input mechanism.
        _keep_playing (boolean): Whether or not the game can continue.
        _output_service (OutputService): The output mechanism.
        _score (Score): an instance of Score.
        _Word (Words): an instance of Words.
    '''

    # Shane
    def __init__(self, input_service, output_service):
        # Needs to include all class attributes
        pass

    # Josh
    def start_game(self):
        # while loop that calls get_inputs, do_updates, and do_outputs
        pass

    # Larry
    def _get_input(self):
        # set key equal to input_service.get_letter()
        # pass key to add_letter in buffer

        # loop through each word in words
            # set words.move_word(random direction)
        pass

    # Shane
    def _do_updates(self):
        # call handle_enter
        pass

    # Brian
    def _do_outputs(self):
        # _output_service.clear_screen()
        # draw the buffer actor
        # draw all words actors
        # draw score actor
        # output_service.flush_buffer()
        pass

    # Vanessa
    def _handle_enter(self):
        # word set it equal to buffer.get_word
        # if * in word
            # new_word set it equal to word with the * removed
            # set points equal to words.word_check(new_word)
            # _score.add_points(points)
            # _buffer.reset()
        word = self.buffer.get_word()
        if '*' in word:
            new_word = word - '*'
            points = self.words.word_check(new_word)
            self._score.add_points(points)
            self._buffer.reset()

        pass
