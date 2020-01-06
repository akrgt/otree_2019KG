from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_trial'
    players_per_group = 2
    num_rounds = 1

    endowment = c(10)


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):

    proposal = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)),
        label="あなたはいくら相手に渡しますか？",
    )

    accepted_or_not = models.BooleanField(
        doc="あなたは提案を受け入れますか？"
    )
    proposer_point = models.CurrencyField()
    accepter_point = models.CurrencyField()


    def compute(self):
        if self.accepted_or_not==True:
            self.proposer_point = Constants.endowment - self.proposal
            self.accepter_point = self.proposal
        else:
            self.proposer_point = 0
            self.accepter_point = 0



class Player(BasePlayer):
    pass
