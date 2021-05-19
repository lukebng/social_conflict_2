from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId='111111a'))
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId=0000000))
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId=7654321))
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId=12345678))
        yield IDPage, dict(DecisionLabId=1111111)
        expect(self.player.DecisionLabId, '1111111')
        #expect(self.player.Dec, '1111111')