from otree.api import *

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


def group_by_arrival_time_method(subsession, waiting_players):
    import itertools
    treats = itertools.cycle(['random', 'same'])
    for p1 in waiting_players:
        for p2 in waiting_players:
            if p1.participant.partner == p2.participant.label:
                p1.treat = next(treats)
                p2.treat = p1.treat
                return [p1, p2]


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.treat == 'random':
            upcoming_apps[randomgroup]
        elif player.treat == 'same'


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [GroupingWaitPage, ResultsWaitPage, Results]
