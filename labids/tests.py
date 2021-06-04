from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):

    cases = ['basic', 'dictator_timeout_1', 'dictator_timeout_2', 'no_partner_round2_dictator',
             'no_partner_round2_recipient']

    def play_round(self):
        yield SubmissionMustFail(IDPage, dict(DecisionLabId='111111a'))
        yield SubmissionMustFail(IDPage, dict(DecisionLabId=0000000))
        yield SubmissionMustFail(IDPage, dict(DecisionLabId=7654321))
        yield SubmissionMustFail(IDPage, dict(DecisionLabId=12345678))
        yield IDPage, dict(DecisionLabId=1234555)
        expect(self.player.DecisionLabId, '1234555')