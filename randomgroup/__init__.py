import random

from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'RaCo'
    players_per_group = 2
    num_rounds = 2
    endowment = Currency(100)


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
    to = models.BooleanField(initial=False)
    confl = make_likert("")
    bad = make_likert("")
    good = make_likert("")
    satisfied = make_likert("")
    regret = make_likert("")
    p_a = make_likert("")
    p_a_o = make_likert("")
    fin1 = models.IntegerField(initial=0)
    fin2 = models.IntegerField(initial=0)


# FUNCTIONS
def group_by_arrival_time_method(subsession, waiting_players):
    if subsession.round_number == 1:
        if len(waiting_players) >= 2:
            p1 = waiting_players[0]
            p2 = waiting_players[1]
            p1.participant.role = 1
            p2.participant.role = 2
            p1.participant.partner = p2.participant.label
            p2.participant.partner = p1.participant.label
            print('partner of p1 is ', p1.participant.partner)
            print('partner of p2 is ', p2.participant.partner)
            return waiting_players[:2]
        for player in waiting_players:
            if waiting_too_long(player):
                # make a single-player group.
                return [player]
    elif subsession.round_number == 2:
        d_players = [p for p in waiting_players if p.participant.role == 1]
        r_players = [p for p in waiting_players if p.participant.role == 2]
        print(d_players)
        print(r_players)
        if len(waiting_players) >= 1:
            if len(d_players) >= 1 and len(r_players) >= 1:
                for i in range(len(d_players)):
                    for j in range(len(r_players)):
                        print('i is ', i)
                        print('j is ', j)
                        if d_players[i].participant.partner != r_players[j].participant.label:
                            return d_players[i], r_players[j]
        for player in waiting_players:
            if waiting_too_long(player):
                return [player]


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if p1.to:
        p1.payoff = 0
    else:
        p1.payoff = Constants.endowment - p1.offer
        p2.payoff = p1.offer


def waiting_too_long(player):
    participant = player.participant
    import time
    return time.time() - participant.wait_page_arrival > 300


def custom_export(players):
    # header row
    yield ['DLCID', 'part_code', 'role', 'partner', 'transfer', 'expconf', 'objctbad', 'objctgood', 'Dsatisfac',
           'Dregret', 'sameagain', 'othragain','payoff', 'final_payoff', 'timeout', 'sessionid', 'id_in_sess', 'group',
           'finished1', 'finished2']
    for p in players:
        participant = p.participant
        session = p.session
        yield [participant.DecisionLabID, participant.code, participant.role, participant.partner, p.offer, p.confl,
               p.bad, p.good, p.satisfied, p.regret, p.p_a_o_50, p.payoff.to_real_world_currency(session),
               participant.payoff_plus_participation_fee(), participant.timo, session.code, participant.id_in_session,
               p.group, p.fin1, p.fin2]


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def before_next_page(player, timeout_happened):
        import time
        player.participant.wait_page_arrival = time.time()

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        group = player.group
        if len(group.get_players()) == 1:
            return "showup"

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            return {
                'body_text': "Ihnen wird nun eine Person zugeteilt. Sobald die nächste Person eintrifft, geht es los.",
                'title_text': "Bitte warten Sie.",
            }
        elif player.round_number == 2:
            return {
                'body_text': "Ihnen wird nun eine andere Person als in Runde 1 zugeteilt. Sobald die nächste Person eintrifft, geht es los.",
                'title_text': "Bitte warten Sie.",
            }


class PlayerA_Offer(Page):
    form_model = 'player'
    form_fields = ['offer']

    timeout_seconds = 300

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.to = True
            player.participant.timo = True
        else:
            print("RaCo: In round ", player.round_number, "player ", player.participant.label, " is in group with ",
                  player.get_others_in_group()[0].participant.label)

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == 1


class ResultsWaitPageRandom(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    @staticmethod
    def before_next_page(player, timeout_happened):
        print("Payoff of ", player.participant.label, " in this round is ", player.payoff)

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if waiting_too_long(player):
            return "showup"
        if player.to:
            return "showup"

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            return {
            'body_text': "Ihnen wurde die Rolle B zugewiesen. Person A entscheidet nun über den Betrag, der an Sie abgeben wird.",
            'title_text': "Bitte warten Sie.",
            }
        if player.round_number == 2:
            return {
            'body_text': "Ihnen wurde nun erneut die Rolle B zugewiesen. Die neu zugeteilte Person A entscheidet nun wieder über den Betrag, der an Sie abgeben wird.",
            'title_text': "Bitte warten Sie.",
            }


class PlayerA_CBG(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class PlayerA_SRPP(Page):
    form_model = 'player'
    form_fields = ['satisfied', 'regret']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.fin1 = 1
        import time
        player.participant.wait_page_arrival = time.time()

    @staticmethod
    def vars_for_template(player: Player):
        return dict(kept=Constants.endowment - player.offer, offer=player.offer)


class PlayerB_CBGPP(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good', 'p_a', 'p_a_o']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == 2 and player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        return dict(kept=Constants.endowment - p1.offer, offer=p1.offer)


class PlayerB_CBGPP2(Page):
    form_model = 'player'
    form_fields = ['confl', 'bad', 'good', ]

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == 2 and player.round_number == 2

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.fin = 1
        import time
        player.participant.wait_page_arrival = time.time()


    @staticmethod
    def vars_for_template(player: Player):
        p1 = player.group.get_player_by_id(1)
        return dict(kept=Constants.endowment - p1.offer, offer=p1.offer)



class Debriefing(Page):
    @staticmethod
    def vars_for_template(player: Player):
        prev_player = player.in_round(player.round_number - 1)
        pp1 = prev_player.group.get_player_by_id(1)
        p1 = player.group.get_player_by_id(1)
        p2 = player.group.get_player_by_id(2)
        kept1 = (Constants.endowment - pp1.offer).to_real_world_currency(player.session)
        offer1 = pp1.offer.to_real_world_currency(player.session)
        kept2 = (Constants.endowment - p1.offer).to_real_world_currency(player.session)
        offer2 = p1.offer.to_real_world_currency(player.session)
        return dict(
            kept1=kept1,
            offer1=offer1,
            kept2=kept2,
            offer2=offer2,
            total_kept=kept1+kept2,
            total_offer=offer1+offer2,
            total_p1=p1.participant.payoff_plus_participation_fee().to_real_world_currency(player.session),
            total_p2=p2.participant.payoff_plus_participation_fee().to_real_world_currency(player.session),
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2


page_sequence = [
    GroupingWaitPage,
    PlayerA_Offer,
    ResultsWaitPageRandom,
    PlayerA_CBG,
    PlayerA_SRPP,
    PlayerB_CBGPP,
    PlayerB_CBGPP2,
    Debriefing,
]
