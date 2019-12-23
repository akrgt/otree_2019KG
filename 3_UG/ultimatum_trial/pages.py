from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    pass

class Page2(Page):
  timeout_seconds = 60
  form_model = 'group'
  form_fields = ['proposal']

  def is_displayed(self):
      return self.player.id_in_group == 1

class Page3(WaitPage):
    pass


class Page4(Page):
  timeout_seconds = 60
  form_model = 'group'
  form_fields = ['accepted_or_not']

  def is_displayed(self):
      return self.player.id_in_group == 2

class Page5(WaitPage):
  def after_all_players_arrive(self):
      self.group.compute()

class Page6(Page):
    pass


page_sequence = [
    Page1,
    Page2,
    Page3,
    Page4,
    Page5,
    Page6
]
