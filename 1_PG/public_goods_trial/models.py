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
公共財ゲーム4人条件
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_trial'
    players_per_group = 4 # 4人プレイヤー
    num_rounds = 1 # 1shotゲーム

    endowment = c(20) # 初期保有額は20ポイント
    multiplier = 2 # 全員の貢献額を2倍にします．


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def compute(self):
        contributions = [p.contribution for p in self.get_players()]
        self.total_contribution = sum(contributions)
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group

        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share



class Player(BasePlayer):
    contribution = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)),
        label="あなたはいくら貢献しますか？"
    )
