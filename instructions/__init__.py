from otree.api import *
import itertools

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )
    q2 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(
        choices=[[0, '0 Cent'], [50, '50 Cent'], [100, '100 Cent']], widget=widgets.RadioSelect
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    pass

treats = itertools.cycle(['random', 'same'])

class Understanding(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3']

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            q1=50,
            q2=100,
            q3=0,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Ihre Antwort war nicht korrekt. Überdenken Sie Ihre Antwort erneut.'

        return error_messages

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.participant.wait_page_arrival = time.time()
        player.participant.timo = False

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        player.participant.treat = next(treats)
        if player.participant.treat == 'random':
            print("participant ", player.participant.label, " has treat ", player.participant.treat)
            return "randomgroup"
        elif player.participant.treat == 'same':
            print("participant ", player.participant.label, " has treat ", player.participant.treat)
            return "samegroup"


page_sequence = [Instructions, Understanding]
