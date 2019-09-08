"""Example to understand strategy pattern. It is a behavioural pattern."""

"""
What is strategy pattern?
Let's divide the definition into three parts:
1) Defines a list of algorithm(or rules) and encapsulate them.
2) Algorithm can be used interchangably.
3) Algorithm will vary independently from clients that use it.

Okay, below example will explain each and every part of the pattern.

Example: A game has various character and each character has its own attack and defend policy.
"""

from abc import ABCMeta

# Lets define the first and second part of the definition.
# Here we define list of attack/defend algorithm.
class AttackStrategy(ABCMeta):
    def attack(self):
        pass


class ChokeslamAttack(AttackStrategy):

    def attack(self):
        print("CHOKESLAM")


class StunnerAttack(AttackStrategy):

    def attack(self):
        print("STUNNER")


class DefendStrategy(ABCMeta):
    def defend(self):
        pass


class SimpleDefend(DefendStrategy):
    def defend(self):
        print("SIMPLE")

class AdvanceDefend(DefendStrategy):
    def defend(self):
        print("ADVANCE")



# Third part of the definition.
# As you can see that we are injecting the behaviour(Composition and not inheritence) of attack
# and defend in `HeroOne` class.
# Algorithm like (attack/defend) can now vary independently irrespective of any client(HeroOne)
# change.
class Person(ABCMeta):
    def attack(self):
        pass

    def defend(self):
        pass


class HeroOne(Person):

    def __init__(self, attack, defend):
        self.attack = attack
        self.defend = defend

    def attack(self):
        self.attack.attack()

    def defend(self):
        self.defend.defend()
