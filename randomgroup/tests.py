from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            if self.player.participant.treat == 'random':
                if self.player.id_in_group == 1:
                    yield PlayerA_Offer, dict(offer=cu(20))
                    expect(self.player.payoff, Constants.endowment - self.player.offer)
                    yield PlayerA_CBG, dict(confl=3, bad=5, good=7)
                    expect(self.player.confl, 3)
                    expect(self.player.bad, 5)
                    expect(self.player.good, 7)
                    yield PlayerA_SRPP, dict(satisfied=1, regret=5)
                    expect(self.player.satisfied, 1)
                    expect(self.player.regret, 5)
                if self.player.id_in_group == 2:
                    expect(self.player.payoff, self.player.group.get_player_by_id(1).offer)
                    yield PlayerB_CBGPP, dict(confl=3, bad=5, good=7, p_a=7, p_a_o=3)
                    expect(self.player.confl, 3)
                    expect(self.player.bad, 5)
                    expect(self.player.good, 7)
                    expect(self.player.p_a, 7)
                    expect(self.player.p_a_o, 3)
        elif self.round_number == 2:
            if self.player.participant.treat == 'random':
                if self.player.id_in_group == 1:
                    yield PlayerA_Offer, dict(offer=cu(40))
                    expect(self.player.payoff, Constants.endowment - self.player.offer)
                    yield PlayerA_CBG, dict(confl=3, bad=5, good=7)
                    expect(self.player.confl, 3)
                    expect(self.player.bad, 5)
                    expect(self.player.good, 7)
                    yield PlayerA_SRPP, dict(satisfied=1, regret=5)
                    expect(self.player.satisfied, 1)
                    expect(self.player.regret, 5)
                if self.player.id_in_group == 2:
                    expect(self.player.payoff, self.player.group.get_player_by_id(1).offer)
                    yield PlayerB_CBGPP2, dict(confl=3, bad=5, good=7)
                    expect(self.player.confl, 3)
                    expect(self.player.bad, 5)
                    expect(self.player.good, 7)
        expect(self.player.participant.payoff_plus_participation_fee(),
               self.player.participant.payoff.to_real_world_currency(self.session)
               + self.player.session.config['participation_fee'])