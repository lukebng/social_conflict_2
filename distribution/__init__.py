from otree.api import *
import itertools

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'distribution'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class WaitPage1(WaitPage):
pass



page_sequence = [WaitPage1]
