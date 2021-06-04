from . import *


class PlayerBot(Bot):

    cases = ['basic', 'dictator_timeout_1', 'dictator_timeout_2', 'no_partner_round2_dictator', 'no_partner_round2_recipient']

    def play_round(self):
        if self.round_number == 1:
            if self.player.participant.treat == 'random':
                if self.player.id_in_group == 1:
                    if self.case == 'dictator_timeout_1':
                        from otree.api import Submission
                        yield Submission(PlayerA_Offer, timeout_happened=True)
                    elif not self.case == 'no_partner_round2_recipient':
                        yield PlayerA_Offer, dict(offer=cu(20))
                        expect(self.player.payoff, Constants.endowment - self.player.offer)
                        yield PlayerA_CBG, dict(confl=3, bad=5, good=7)
                        expect(self.player.confl, 3)
                        expect(self.player.bad, 5)
                        expect(self.player.good, 7)
                        yield PlayerA_SRPP, dict(satisfied=1, regret=5)
                        expect(self.player.satisfied, 1)
                        expect(self.player.regret, 5)
                        if self.case == 'basic':
                            expect(self.player.participant.payoff_plus_participation_fee(), self.player.participant.payoff.to_real_world_currency(self.session) + self.player.session.config['participation_fee'])
                if self.player.id_in_group == 2:
                    if not self.case == 'no_partner_round2_dictator':
                        expect(self.player.payoff, self.player.group.get_player_by_id(1).offer)
                        yield PlayerB_CBGPP, dict(confl=3, bad=5, good=7, p_a=7, p_a_o=3)
                        expect(self.player.confl, 3)
                        expect(self.player.bad, 5)
                        expect(self.player.good, 7)
                        expect(self.player.p_a, 7)
                        expect(self.player.p_a_o, 3)
                        yield PlayerB_Alt0, dict(confl_0=3, bad_0=5, good_0=7, p_a_0=7, p_a_o_0=3)
                        expect(self.player.confl_0, 3)
                        expect(self.player.bad_0, 5)
                        expect(self.player.good_0, 7)
                        expect(self.player.p_a_0, 7)
                        expect(self.player.p_a_o_0, 3)
                        yield PlayerB_Alt25, dict(confl_25=3, bad_25=5, good_25=7, p_a_25=7, p_a_o_25=3)
                        expect(self.player.confl_25, 3)
                        expect(self.player.bad_25, 5)
                        expect(self.player.good_25, 7)
                        expect(self.player.p_a_25, 7)
                        expect(self.player.p_a_o_25, 3)
                        yield PlayerB_Alt50, dict(confl_50=3, bad_50=5, good_50=7, p_a_50=7, p_a_o_50=3)
                        expect(self.player.confl_50, 3)
                        expect(self.player.bad_50, 5)
                        expect(self.player.good_50, 7)
                        expect(self.player.p_a_50, 7)
                        if self.case == 'basic':
                            expect(self.player.participant.payoff_plus_participation_fee(), self.player.participant.payoff.to_real_world_currency(self.session) + self.player.session.config['participation_fee'])
        elif self.round_number == 2:
            if self.player.participant.treat == 'random':
                if self.player.id_in_group == 1:
                    if self.case == 'dictator_timeout_2':
                        from otree.api import Submission
                        yield Submission(PlayerA_Offer, timeout_happened=True)
                    elif not self.case == 'no_partner_round2_recipient':
                        yield PlayerA_Offer, dict(offer=cu(40))
                        expect(self.player.payoff, Constants.endowment - self.player.offer)
                        yield PlayerA_CBG, dict(confl=3, bad=5, good=7)
                        expect(self.player.confl, 3)
                        expect(self.player.bad, 5)
                        expect(self.player.good, 7)
                        yield PlayerA_SRPP, dict(satisfied=1, regret=5)
                        expect(self.player.satisfied, 1)
                        expect(self.player.regret, 5)
                        if self.case == 'basic':
                            expect(self.player.participant.payoff_plus_participation_fee(), self.player.participant.payoff.to_real_world_currency(self.session) + self.player.session.config['participation_fee'])
                if self.player.id_in_group == 2:
                    if not self.case == 'no_partner_round2_dictator':
                        expect(self.player.payoff, self.player.group.get_player_by_id(1).offer)
                        yield PlayerB_CBGPP2, dict(confl=3, bad=5, good=7)
                        expect(self.player.confl, 3)
                        expect(self.player.bad, 5)
                        expect(self.player.good, 7)
                        yield PlayerB_Alt0, dict(confl_0=3, bad_0=5, good_0=7, p_a_0=7, p_a_o_0=3)
                        expect(self.player.confl_0, 3)
                        expect(self.player.bad_0, 5)
                        expect(self.player.good_0, 7)
                        expect(self.player.p_a_0, 7)
                        expect(self.player.p_a_o_0, 3)
                        yield PlayerB_Alt25, dict(confl_25=3, bad_25=5, good_25=7, p_a_25=7, p_a_o_25=3)
                        expect(self.player.confl_25, 3)
                        expect(self.player.bad_25, 5)
                        expect(self.player.good_25, 7)
                        expect(self.player.p_a_25, 7)
                        expect(self.player.p_a_o_25, 3)
                        yield PlayerB_Alt50, dict(confl_50=3, bad_50=5, good_50=7, p_a_50=7, p_a_o_50=3)
                        expect(self.player.confl_50, 3)
                        expect(self.player.bad_50, 5)
                        expect(self.player.good_50, 7)
                        expect(self.player.p_a_50, 7)
                        if self.case == 'basic':
                            expect(self.player.participant.payoff_plus_participation_fee(), self.player.participant.payoff.to_real_world_currency(self.session) + self.player.session.config['participation_fee'])