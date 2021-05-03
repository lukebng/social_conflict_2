from otree.api import *

doc = """
Your app description
"""

#define necessary constants
class Constants(BaseConstants):
    name_in_url = 'SoCO'
    players_per_group = 2
    num_rounds = 1
    endowment = Currency(100)
    dictator_role = 'Dictator'
    recipient_role = 'Recipient'


class Subsession(BaseSubsession):
    pass

#function that returns 10-point Likert-scale
def make_likert(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

#function that returns 7-point Likert-scale
def make_likert_7(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Group(BaseGroup):
    pass

#define player model
class Player(BasePlayer):
    #define offer variable that saves dictator's tranfer
    offer = models.CurrencyField(min=0, max=Constants.endowment, label="")
    #define timeout variable that states if a timeout occured
    to = models.BooleanField()
    #define variables for social conflict items
    confl = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    p_a = make_likert("")
    p_a_o = make_likert("")
    #define variables for alternative amounts displayed to the recipient
    confl_0 = make_likert("")
    confl_25 = make_likert("")
    confl_50 = make_likert("")
    bad_0 = make_likert("")
    bad_25 = make_likert("")
    bad_50 = make_likert("")
    good_0 = make_likert("")
    good_25 = make_likert("")
    good_50 = make_likert("")
    p_a_0 = make_likert("")
    p_a_25 = make_likert("")
    p_a_50 = make_likert("")
    p_a_o_0 = make_likert("")
    p_a_o_25 = make_likert("")
    p_a_o_50 = make_likert("")
    #define trait ambivalence scale items
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
#define function that sets the payoffs for players depending on whether a timeout occurred
def set_payoffs(group: Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        if p1.to:
            p1.payoff = 0
        else:
            p1.payoff = 200 + Constants.endowment - p1.offer
            p2.payoff = 200 + p1.offer

#define a function that checks whether players are waiting too long
def waiting_too_long(player):
    participant = player.participant
    import time
    return time.time() - participant.wait_page_arrival > 180

#define a function that groups players when they arrive at this app
def group_by_arrival_time_method(subsession, waiting_players):
    if len(waiting_players) >= 2:
        p1 = waiting_players[0]
        p2 = waiting_players[1]
        p1.participant.role = 1
        p2.participant.role = 2
        return waiting_players[:2]
    for player in waiting_players:
        if waiting_too_long(player):
            # make a single-player group.
            return [player]

#define custom export for social conflict app
def custom_export(players):
    # header row
    yield ['DLCID', 'role', 'transfer', 'expconf', 'objctbad', 'objctgood', 'Dsatisfac', 'Dregret', 'sameagain',
           ' othragain', 'ambv1', 'ambv2', 'ambv3', 'ambv4', 'ambv5', 'ambv6', 'ambv7', 'ambv8', 'ambv9', 'ambv10',
           'expconf0', 'objbad0', 'objgood0', 'again0', 'othgain0', 'expconf25', 'objbad25', 'objgood25', 'again25',
           'othgain25', 'expconf50', 'objbad50', 'objgood50', 'again50', 'othgain50', 'payoff', 'timeout', 'sessionid',
           'id_in_sess', 'group', 'part_code', 'finished']
    for p in players:
        participant = p.participant
        session = p.session
        yield [participant.label, p.role, p.offer, p.confl, p.bad, p.good, p.satisfied, p.regret, p.p_a, p.p_a_o, p.amb1, p.amb2,
               p.amb3, p.amb4, p.amb5, p.amb6, p.amb7, p.amb8, p.amb9, p.amb10, p.confl_0, p.bad_0, p.good_0, p.p_a_0,
               p.p_a_o_0,  p.confl_25, p.bad_25, p.good_25, p.p_a_25, p.p_a_o_25,  p.confl_50, p.bad_50, p.good_50,
               p.p_a_50, p.p_a_o_50, p.payoff, p.to, session.code, participant.id_in_session, p.group, participant.code, p.fin]


# PAGES
#define Waitpage that groups all players
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    #method that redirects players when odd number
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        group = player.group
        if len(group.get_players()) == 1:
            return upcoming_apps[0]

    #method that changes the text of the waitpage
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'body_text': "Ihnen wird nun eine Person zugeteilt. Sobald die nächste Person eintrifft, geht es los.",
            'title_text': "Bitte warten Sie.",
        }

#page for the dictator to make an offer
class PlayerA_Offer(Page):
    form_model = 'player'
    form_fields = ['offer']

    timeout_seconds = 180

    #checks whether timeout happened and sets timeout variable to true if so
    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.to = True
        else:
            player.to = False

    #function that makes sure to just display page to dictators
    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if waiting_too_long(player):
            return upcoming_apps[-1]

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'body_text': "Ihnen wurde die Rolle B zugewiesen. Person A entscheidet nun über den Betrag, der an Sie abgeben wird.",
            'title_text': "Bitte warten Sie.",
        }


class PlayerA_CBG(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class PlayerA_SRPP(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret', 'p_a', 'p_a_o']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class PlayerB_CBGPP(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good', 'p_a', 'p_a_o']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role

    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        return dict(kept=Constants.endowment - p1.offer, offer=p1.offer)


class PlayerB_Alt0(Page):
    form_model = 'player'
    form_fields = ['confl_0', 'bad_0', 'good_0', 'p_a_0', 'p_a_o_0']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class PlayerB_Alt25(Page):
    form_model = 'player'
    form_fields = ['confl_25', 'bad_25', 'good_25', 'p_a_25', 'p_a_o_25']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class PlayerB_Alt50(Page):
    form_model = 'player'
    form_fields = ['confl_50', 'bad_50', 'good_50', 'p_a_50', 'p_a_o_50']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role


class TAS(Page):
    form_model = 'player'
    form_fields = [
        'amb1',
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


class Debriefing(Page):
    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        return dict(
            kept=(Constants.endowment - p1.offer).to_real_world_currency(player.session),
            offer=p1.offer.to_real_world_currency(player.session),
            total_p1=p1.payoff.to_real_world_currency(player.session),
            total_p2=p2.payoff.to_real_world_currency(player.session),
        )


page_sequence = [
    GroupingWaitPage,
    PlayerA_Offer,
    ResultsWaitPage,
    PlayerA_CBG,
    PlayerA_SRPP,
    PlayerB_CBGPP,
    PlayerB_Alt0,
    PlayerB_Alt25,
    PlayerB_Alt50,
    TAS,
    Debriefing,
]
