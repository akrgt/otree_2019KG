# プログラム④：独裁者ゲーム

## これから作る実験プログラムの概要：

* 2人独裁者ゲーム
* 独裁者の初期保有額を10ポイント
* 独裁者は0-10ポイントの中から好きな金額を提案できる．
* 応答者は提案者の提案に対して何もできず受け入れるのみ
* ページは4ページ
  - Page1：ルール説明のページ
    <img src="picture/Page1.png" alt="Page1" style="zoom:40%;" /> <br><br>
  - Page2：（独裁者のみ）提案額を決定するページ
    <img src="picture/Page2.png" alt="Page2" style="zoom:40%;" /> <br><br>
  - Page3：（応答者のみ）提案者の決定を待つページ
    <img src="picture/Page3.png" alt="Page3" style="zoom:40%;" /> <br><br>
  - Page4：結果を出力するページ
    <img src="picture/Page4.png" alt="Page6" style="zoom:40%;" /> <br><br>



## アプリを作成する

* その前にフォルダを移動します．
  * Windowsの場合
  ```
  cd C:¥Users¥[PC名]¥Desktop¥otreetest
  ```

  * Macの場合
  ```
  cd Desktop/otreetest
  ```


* 土台となるアプリを作成します．
```
otree startapp dictator_trial
```


## modelsの定義：
* models.pyでは動作を定義します．

### Constantsクラスの定義：基本設計

* dictator_trialフォルダ内のmodels.pyを開く
* Constantsクラスの中で人数・繰り返し回数・初期保有額・係数を設定する．

```Python
class Constants(BaseConstants):
    name_in_url = 'dictator_trial'
    players_per_group = 2 # 2人プレイヤー
    num_rounds = 1 # 1shotゲーム

    endowment = c(10) # 提案者の初期保有額は10ポイント
```




### Playerクラスの定義：

* Playerクラスの中で，各プレイヤーに関する変数を定義する．

```Python
class Player(BasePlayer):
  pass
```
  - 今回は全てをGroupクラスの中で定義します．


### Groupクラスの定義
* Groupクラスの中で全てのプレイヤーの変数に影響を及ぼす関数を定義する．

```Python
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
```

* `def`以下では関数を定義している．
  - 「こんな感じで計算してよう！よろしく＼(^o^)／」ということを定義している．


## templatesの定義：
* templatesでは具体的な項目を表示するページに決めていきます．

* `dictator_trial/templates/dictator_trial`の中に`Page1.html`，`Page2.html`，`Page4.html`という4つのhtmlファイルを作成します．
  - `Page1`がルール説明ページ，`Page2`が独裁者の提案額入力ページ，`Page4`が結果の表示ページとなる．
  - 待ちページは追って説明する．


### 1ページ目
```html
{% extends "global/Page.html" %}
{% load otree static %}

{% block title %}
    説明
{% endblock %}
{% block content %}
<p>
    これは独裁者ゲームです．<br>
    このゲームではプレイヤー1とプレイヤー2にランダムに割り振られます．<br>
    それぞれの役割は以下のとおりです．
</p>
<div>
<strong>プレイヤー1に割り振られた場合</strong>
<p>
  あなたは最初{{ Constants.endowment }}を持っています．その中からプレイヤー2にいくら渡すかを決めてもらいます．プレイヤー2には拒否権がありません．したがって，あなたの決定通りに分配が行われます．
</p>
</div>

<div>
<strong>プレイヤー2に割り振られた場合</strong>
<p>
  あなたはプレイヤー1の決定どおりにポイントを受け取ります．
</p>
</div>

    {% next_button %}

{% endblock %}

```



### 2ページ目
```html
{% extends "global/Page.html" %}
{% load otree static %}

{% block title %}
    分配額の決定
{% endblock %}
{% block content %}
<p>
    あなたは<strong>プレイヤー1</strong>に割り振られました
</p>
{% formfields group.proposal %}
    {% next_button %}
{% endblock %}
```

### 3ページ目
* 慌てない

### 4ページ目
```html
{% extends "global/Page.html" %}
{% load otree static %}

{% block title %}
    結果の確認
{% endblock %}

{% block content %}
<p>
    プレイヤー1に対して初期保有額として<strong> {{ Constants.endowment }}</strong>が渡されました．<br>
    プレイヤー1はプレイヤー2に対して<strong>{{ group.proposal }}</strong>を渡すことを提案しました．<br>
    <br>
    その結果，以下の通りの利得配分となりました．<br>
    <br>
    プレイヤー1：{{ group.proposer_point }}<br>
    プレイヤー2：{{ group.accepter_point }}<br>

    {% next_button %}
{% endblock %}

```



## pagesの定義：

* `pages.py`では「ページの表示順」や「入力項目」，**「関数の計算の順番」** などを設定します．
  - 実は**「関数の計算の順番」** がかなりややこしくて難しい．

* `pages.py`で設定する動作
  - `Page1.html`を表示する
    - 独裁者ゲームのルールを説明する
  - `Page2.html`を表示する
    - プレイヤー1(独裁者)にだけ表示する
    - 提案額を入力する
  - `Page3.html`を表示する
    - プレイヤー2(応答者)にだけ表示する
    - プレイヤー1の入力を待つ
  - `Page4.html`を表示する
    - 各自の利益を表示する．


  - `Page1`から`Page4`を順番に表示するように設定する．

### Page1について
* `Page1`は何も入力欄の表示や，計算などの特別な動きはありません．
```Python
class Page1(Page):
    pass
```

### Page2について
* `Page2`では提案額の入力があります．
  - 60秒の時間制限を設定します．
  - 入力画面を作ってあげましょう．
  - 表示されるプレイヤーが限定されます．

```Python
class Page2(Page):
  timeout_seconds = 60
  form_model = 'group'
  form_fields = ['proposal']

  def is_displayed(self):
      return self.player.id_in_group == 1
```

### Page3について
* 全てのプレイヤーが`Page3`に入ります．
  - この中で他のプレイヤーの利得が計算されます．
```
class Page3(WaitPage):
  def after_all_players_arrive(self):
      self.group.compute()
```
  - ここでは特に処理すべきことはありません．

### Page4について

* 実験参加者が入力する項目がない時はpassします．

```Python
class Page4(Page):
    pass
```


### 表示する順番を定義する

* **今回はどこもいじりません．**
* 一番最後に画面を表示する順番を定義します．
```Python
page_sequence = [
    Page1,
    Page2,
    Page3,
    Page4
]
```



## settingにおけるsession configsの定義：

* oTree で実験を実装するには，`settings.py`の中の`SESSION_CONFIGS`にアプリを登録する必要があります．
* ここでは公共財ゲームに追記する形で記載します．

```Python
SESSION_CONFIGS = [
    dict(
        name='PG4',
        display_name="はじめての公共財ゲーム",
        num_demo_participants=4,
        app_sequence=['public_goods_trial']
    ),
    dict(
        name='SD4',
        display_name="はじめての社会的ジレンマ",
        num_demo_participants=4,
        app_sequence=['SD4_trial']
    ),
    dict(
        name='UG',
        display_name="はじめての最終提案ゲーム",
        num_demo_participants=2,
        app_sequence=['ultimatum_trial']
    ),
    dict(
        name='DG',
        display_name="はじめての独裁者ゲーム",
        num_demo_participants=2,
        app_sequence=['dictator_trial']
    ),]
```


## サーバとして起動
* 自身の端末をサーバとして起動します．
```Python
otree devserver
```
  - これで自身の端末で実験を実施することができます．
  - [http://localhost:8000/](http://localhost:8000/)にアクセスしてみてください．







## 全てのコード

[ダウンロード](UG_trial.zip)
