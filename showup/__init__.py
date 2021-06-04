from otree.api import *
c = Currency

doc = """
Your app description
"""

#define constants
class Constants(BaseConstants):
    name_in_url = 'showup'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

#function that returns 7-point Likert-scale
def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

#FUNCTIONS
#define custom export for showup fee app
def custom_export(players):
    # header row
    yield ['DLCID', 'payoff', 'sessionid', 'id_in_session', 'part_code']
    for p in players:
        participant = p.participant
        session = p.session
        yield [participant.label, p.payoff, session.code, participant.id_in_session, participant.code]

# PAGES
#define showup fee page
class Showup(Page):
    #provide variables for showup fee page
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            total_earnings=player.participant.payoff_plus_participation_fee().to_real_world_currency(player.session),
            timeout=player.participant.vars.get('timo'),
        )


page_sequence = [
    Showup,
]
