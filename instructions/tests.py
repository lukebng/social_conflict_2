from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Instructions
        yield SubmissionMustFail(Understanding, dict(q1=100, q2=100, q3=0))
        yield SubmissionMustFail(Understanding, dict(q1=0, q2=100, q3=0))
        yield SubmissionMustFail(Understanding, dict(q1=50, q2=50, q3=0))
        yield SubmissionMustFail(Understanding, dict(q1=50, q2=0, q3=0))
        yield SubmissionMustFail(Understanding, dict(q1=50, q2=100, q3=100))
        yield SubmissionMustFail(Understanding, dict(q1=50, q2=100, q3=50))
        yield Understanding, dict(q1=50, q2=100, q3=0)
        expect(self.player.q1, 50)
        expect(self.player.q2, 100)
        expect(self.player.q3, 0)