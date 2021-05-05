from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
            yield PlayerA_Offer, dict(offer=cu(34))
            expect(self.player.payoff, 200 + Constants.endowment - self.player.offer)
            yield PlayerA_CBG, dict(confl=3, bad=5, good=7)
            expect(self.player.confl, 3)
            expect(self.player.good, 5)
            expect(self.player.bad, 7)
            yield PlayerA_SRPP, dict(satified=1, regret=5, p_a=7, p_a_o=3)
            expect(self.player.satisfied, 1)
            expect(self.player.regret, 5)
            expect(self.player.p_a, 7)
            expect(self.player.p_a, 3)
            yield TAS, dict(amb1=2, amb2=4, amb3=6, amb4=5, amb5=3, amb6=1, amb7=1, amb8=6, amb9=3, amb10=7)
            expect(self.player.amb1, 2)
            expect(self.player.amb2, 4)
            expect(self.player.amb3, 6)
            expect(self.player.amb4, 5)
            expect(self.player.amb5, 3)
            expect(self.player.amb6, 1)
            expect(self.player.amb7, 1)
            expect(self.player.amb8, 6)
            expect(self.player.amb9, 3)
            expect(self.player.amb10, 7)