from otree.api import Currency as c, currency_range, expect, Bot
from . import *

cases = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
class PlayerBot(Bot):
    def play_round(self):
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId='111111a'))
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId=0000000))
            #yield SubmissionMustFail(IDPage, dict(DecisionLabId=7654321))
            yield SubmissionMustFail(IDPage, dict(DecisionLabId=12345678))
            if self.case == 'a':
                yield IDPage, dict(DecisionLabId=1111111)
                expect(self.player.DecisionLabId, '1111111')
                expect(self.player.participant.label, '1111111')
            if self.case == 'b':
                yield IDPage, dict(DecisionLabId=2222222)
                expect(self.player.DecisionLabId, '2222222')
                expect(self.player.participant.label, '2222222')
            if self.case == 'c':
                yield IDPage, dict(DecisionLabId=3333333)
                expect(self.player.DecisionLabId, '3333333')
                expect(self.player.participant.label, '3333333')
            if self.case == 'd':
                yield IDPage, dict(DecisionLabId=4444444)
                expect(self.player.DecisionLabId, '4444444')
                expect(self.player.participant.label, '4444444')
            if self.case == 'e':
                yield IDPage, dict(DecisionLabId=5555555)
                expect(self.player.DecisionLabId, '5555555')
                expect(self.player.participant.label, '5555555')
            if self.case == 'f':
                yield IDPage, dict(DecisionLabId=6666666)
                expect(self.player.DecisionLabId, '6666666')
                expect(self.player.participant.label, '6666666')
            if self.case == 'g':
                yield IDPage, dict(DecisionLabId=7777777)
                expect(self.player.DecisionLabId, '7777777')
                expect(self.player.participant.label, '7777777')
            if self.case == 'h':
                yield IDPage, dict(DecisionLabId=8888888)
                expect(self.player.DecisionLabId, '8888888')
                expect(self.player.participant.label, '8888888')
