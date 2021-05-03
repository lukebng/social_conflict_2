from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(
        choices=[
            [True, 'Ja, ich bin damit einverstanden.'],
            [False, 'Nein, ich bin damit nicht einverstanden.'],
        ],
        widget=widgets.RadioSelect,
        label="",
    )


# FUNCTIONS
# PAGES
class Introduction(Page):
    pass


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def error_message(player, values):
        if not values['consent']:
            return (
                "Um an der Studie teilzunehmen müssen Sie der Einverständniserklärung zustimmen. "
                "Andernfalls schließen Sie das Fenster um die Studie an dieser Stelle zu beenden. "
                "Ihre Entlohnung entfällt hierbei jedoch."
            )


page_sequence = [Introduction, Consent]
