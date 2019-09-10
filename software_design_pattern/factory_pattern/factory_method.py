"""Example to understand factory method design pattern. It is a creational pattern."""

"""
Problem: Create character randomly based on game level(easy/hard).

Why to use it:
1) To encapsulate the creation of object at one place, so that it can be reused.
2) To make use of polymorphism, so that we can change the logic of object creation without
much changing the client code. 
"""

from abc import ABC, abstractmethod
import random


# Implementation of player class.
class Player(ABC):
    def action(self):
        pass


class Hero(Player):
    def action(self):
        # Some implementation.
        pass


class Villian(Player):
    def action(self):
        # Some implementation.
        pass


############ Factory Start #############
# Factory to generate Player class.
class PlayerFactory(ABC):
    def create_player(self):
        pass


class EasyGamePlayerFactory(PlayerFactory):
    """For game level easy probability of generating `Heros` are more that `Villian`."""
    def create_player(self):
        player = random.choices([Hero, Hero, Villian])
        return player()


class ToughGamePlayerFactory(PlayerFactory):
    def create_player(self):
        """For game level easy probability of generating `Villian` are more that `Hero`."""
        player = random.choices([Hero, Villian, Villian])
        return player()

############ Factory End #############


############ Client Code Start #############
class StartGame:
    """
    How factory helps:
    1. In future, if we introduce the new way of player creation, we just have
       to introduce the new factory class(`polymorphism` :)).
    2. The logic of player creation is at different place (not the headache for client).
       If new game is introduced, the factory logic can be reused.
    """

    def main(self, type):
        # Place where player is created.
        if type == 'easy':
            player = EasyGamePlayerFactory()
        elif type == 'hard':
            player = ToughGamePlayerFactory()

############ Factory Code End #############
