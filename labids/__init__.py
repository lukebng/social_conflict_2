from string import digits

from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'LabIDs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    DecisionLabId = models.CharField(max_length=7)


# FUNCTIONS
def DecisionLabId_error_message(player: Player, value):
    # Exactly 7 digits
    if len(value) < 7:
        return "Eingabe zu kurz! Die Decision Lab Id sollte genau sieben Stellen haben!"
    # Only digits
    if any([c not in digits for c in value]):
        return "Bitte nur Ziffern eingeben!"
    # Last two digits are the sum of all other digits
    sm = sum([int(c) * (i + 1) for i, c in enumerate(value[0:5])]) % 100
    if not sm == int(value[5:]):
        return "Falsche Decision Lab ID!"
    if value == "0000000":
        return "Fehlerhafe Decision Lab ID!"
    # Already participated
    with open('labids/Participated.txt', 'r') as file:
        txt = file.read()
    if(value in txt and value != "1234555"):
        return "An dieser Studie haben Sie bereits teilgenommen!"


# PAGES
class IDPage(Page):
    form_model = 'player'
    form_fields = ['DecisionLabId']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.DecisionLabID = player.DecisionLabId
        player.participant.label = player.DecisionLabId

page_sequence = [IDPage]
