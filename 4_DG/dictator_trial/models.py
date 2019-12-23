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
    name_in_url = 'dictator_trial'
    players_per_group = 2 # 2人プレイヤー
    num_rounds = 1 # 1shotゲーム

    endowment = c(10) # 提案者の初期保有額は10ポイント


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
# プレイヤーの選択を定義する．
## プレイヤー1の選択は提案額を決める．
    proposal = models.CurrencyField(
        choices=currency_range(c(0), c(Constants.endowment), c(1)),
        label="あなたはいくら相手に渡しますか？",
    )
    proposer_point = models.CurrencyField() # プレイヤー1の利得
    accepter_point = models.CurrencyField() # プレイヤー2の利得

# 計算を実行する
    def compute(self):
        self.proposer_point = Constants.endowment - self.proposal #プレイヤー1の初期保有額-プレイヤー2への提案額
        self.accepter_point = self.proposal #プレイヤー2への提案額




class Player(BasePlayer):
    pass
