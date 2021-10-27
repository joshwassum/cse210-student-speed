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

    def __init__(self, input_service, output_service):
        pass

    def start_game(self):
        pass

    def _get_input(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass

    def _handle_enter(self):
        pass
