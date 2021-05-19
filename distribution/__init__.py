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


def creating_session(subsession):
    treats = itertools.cycle(['random', 'same'])
    for player in subsession.get_players():
        player.participant.treat = next(treats)


# PAGES
class GroupingWaitPage(WaitPage):

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.participant.treat == 'random':
            print("participant ", player.participant.label, " has treat ", player.participant.treat)
            return "randomgroup"
        elif player.participant.treat == 'same':
            print("participant ", player.participant.label, " has treat ", player.participant.treat)
            return "samegroup"


page_sequence = [GroupingWaitPage]
