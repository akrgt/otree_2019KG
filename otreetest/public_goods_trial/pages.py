from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = 'player'
    form_fields = ['contribution']

class Page2(WaitPage):

    def after_all_players_arrive(self):
        self.group.compute()

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Page3(Page):
    pass


page_sequence = [
    Page1,
    Page2,
    Page3
]
