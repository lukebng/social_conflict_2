from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hypothetical'
    players_per_group = None
    num_rounds = 1
    endowment = Currency(100)
    rolehypo = 'Dictator'


class Subsession(BaseSubsession):
    pass


def make_likert(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    offer = models.CurrencyField(min=0, max=Constants.endowment, label="")
    confl = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    p_a = make_likert("")
    p_a_o = make_likert("")
    amb1 = make_likert_7("")
    amb2 = make_likert_7("")
    amb3 = make_likert_7("")
    amb4 = make_likert_7("")
    amb5 = make_likert_7("")
    amb6 = make_likert_7("")
    amb7 = make_likert_7("")
    amb8 = make_likert_7("")
    amb9 = make_likert_7("")
    amb10 = make_likert_7("")
    fin = models.IntegerField(initial=0)

# FUNCTIONS

def custom_export(players):
    # header row
    yield ['DLCID', 'role', 'transfer', 'expconf', 'objctbad', 'objctgood', 'Dsatisfac', 'Dregret', 'sameagain',
           'othragain', 'ambv1', 'ambv2', 'ambv3', 'ambv4', 'ambv5', 'ambv6', 'ambv7', 'ambv8', 'ambv9', 'ambv10',
           'payoff', 'sessionid', 'id_in_sess', 'part_code', 'finished']
    for p in players:
        participant = p.participant
        session = p.session
        yield [participant.label, Constants.rolehypo, p.offer, p.confl, p.bad, p.good, p.satisfied, p.regret,
               p.p_a, p.p_a_o, p.amb1, p.amb2, p.amb3, p.amb4,
               p.amb5, p.amb6, p.amb7, p.amb8, p.amb9, p.amb10, p.payoff,
               session.code, participant.id_in_session, participant.code, p.fin]

# PAGES
class hypothetical(Page):
    pass


class PlayerA_Offer(Page):
    form_model = 'player'
    form_fields = ['offer']


class PlayerA_CBG(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class PlayerA_SRPP(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'p_a', 'p_a_o']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class TAS(Page):
    form_model = 'player'
    form_fields = [
        'amb1',
        'amb2',
        'amb2',
        'amb3',
        'amb4',
        'amb5',
        'amb6',
        'amb7',
        'amb8',
        'amb9',
        'amb10',
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.fin = 1
        player.payoff = 250


class Debriefing(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            total_p1=player.payoff.to_real_world_currency(player.session),
        )


page_sequence = [
    hypothetical,
    PlayerA_Offer,
    PlayerA_CBG,
    PlayerA_SRPP,
    TAS,
    Debriefing,
]
