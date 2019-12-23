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
  def after_all_players_arrive(self):
      self.group.compute()

class Page4(Page):
    pass


page_sequence = [
    Page1,
    Page2,
    Page3,
    Page4
]
