from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):

    cases = ['basic', 'dictator_timeout_1', 'dictator_timeout_2', 'no_partner_round2_dictator',
             'no_partner_round2_recipient']

    def play_round(self):
            yield Introduction
            yield SubmissionMustFail(Consent, dict(consent=False))
            yield Consent, dict(consent=True)
            expect(self.player.consent, True)