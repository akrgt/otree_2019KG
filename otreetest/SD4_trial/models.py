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


author = 'Akira GOTO'

doc = """
社会的ジレンマ4人条件
"""


class Constants(BaseConstants):
    name_in_url = 'SD4_trial'
    players_per_group = 4 # 4人プレイヤー
    num_rounds = 1 # 1shotゲーム

    endowment = c(20) # 初期保有額は20ポイント
    multiplier = 2 # 全員の貢献額を2倍にします．


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    N_of_NoContribution = models.IntegerField()
    N_of_Contribution = models.IntegerField()


    def compute(self):
        contributions = [p.contribution for p in self.get_players()]
        self.total_contribution = sum(contributions)
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        self.N_of_NoContribution = contributions.count(0)
        self.N_of_Contribution = Constants.players_per_group - self.N_of_NoContribution

        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share



class Player(BasePlayer):
    contribution = models.CurrencyField(
        choices=[
            [c(0),'協力する'],
            [c(Constants.endowment), '協力しない']
            ],
        label="あなたは協力しますか？協力しませんか？",
        widget=widgets.RadioSelect
    )
