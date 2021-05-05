from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
            if self.player.id_in_group == 2:
                yield Showup
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