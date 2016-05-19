#!/usr/bin/env
from datetime import datetime


class PlayerOutOfBoundsError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class TurnOutOfBoundsError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OutOfBoardError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Game:
    """
    The Tic-Tac-Toe game itself. Also known as the board.
    """
    winner = None
    createdAt = None
    endedAt = None
    players = []

    def __init__(self):
        self.createdAt = datetime.now()

    def add_player(self, name):
        """
        Adds a player to the game. The game may not contain more than two players.
        :param name: the name of the player to be inserted
        :return: returns true if adding the player was successful
        """
        # The amount of players in the game currently
        amount_of_players = len(self.players)

        if amount_of_players < 2:
            self.players.append(Player(name))
            return True
        else:
            raise PlayerOutOfBoundsError('Trying to add a player above the limit.')


class Player:
    """
    A player participates in a game. A game has exactly two players.
    It's impossible for a player to have more than 5 turns, since there
    are only 9 spots on the board for 2 players.
    """

    def __init__(self, name):
        self.createdAt = datetime.now()
        self.turns = 5
        self.turnHistory = []
        self.name = name

    def create_turn(self):
        """
        Creates a turn and adds it to the turn history.
        A player may not have more than 5 turns.
        :return:
        """
        if len(self.turnHistory) < 5:
            turn = Turn()
            self.turnHistory.append(turn)
            return turn
        else:
            raise TurnOutOfBoundsError('Attempted to do a sixth turn, not possible.')

    def get_current_turn(self):
        """
        Returns the current turn of the player, this is the last one added.
        :return:
        """
        return self.turnHistory[-1]


class Turn:
    """
    A turn in a game. A turn is created and executed by a player. A turn contains meta data about the turn.
    """

    def __init__(self):
        self.createdAt = datetime.now()
        self.executedAt = None
        self.location = None

    def execute_turn(self, x, y):
        """
        The user actively executes the turn, choosing a position on the board.
        executedAt variable should be filled here
        :param x: horizontal index value of the board, must be either 1, 2 or 3
        :param y: vertical index value of the board, must be either 1, 2 or 3
        :return:
        """
        valid_x_indexes = [1, 2, 3]
        valid_y_indexes = [1, 2, 3]
        if x not in valid_x_indexes:
            raise OutOfBoardError('X value was not placed on board')
        if y not in valid_y_indexes:
            raise OutOfBoardError('Y value was not placed on board')

        self.location = Location(x, y)
        self.executedAt = datetime.now()

    def get_time_taken(self):
        return (self.createdAt - self.executedAt).total_seconds()


class Location:
    """
    The location of the X or O placed by the player.
    """
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

# class TestClass:
#     """
#     Testing purposes
#     """
#     x = None
#
#     def __init__(self):
#         print('x before init;', self.x)
#         self.x = 'Initialized in __init__'
#         print('x after init;', self.x, '\n')
#
#     def method_assign_value(self):
#         print('before assign value;', self.x)
#         self.x = 'value assigned in method'
#         print('self x before method;', self.x, '\n')
#
#     def method_set_value_none(self):
#         print('before assign none;', self.x)
#         self.x = None
#         print('after assign none;', self.x, '\n')
#
#
# test = TestClass()
# print(test.x, '\n')
# test.method_assign_value()
# print(test.x, '\n')
# test.method_set_value_none()
# print(test.x, '\n')
