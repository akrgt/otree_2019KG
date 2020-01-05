その他Tips

### 日本語にしよう
* `settings.py`の中で書き換えるといける．

```
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja' # 最初はenになっている．

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY' # 最初はUSDになっている．
USE_POINTS = True
```
* ちなみに，ここでは「ポイント」を使っているけど，円表記も可能．



### 実際のプログラムでのインストラクション

* 実は最初のルール説明用画面とインストラクションを別に作っている．
  - インストラクションは常には表示したくないけど，必要なときには表示できるようにしたい．
  
  - 埋め込み表示ができるので，最初のルール説明用画面に別途ファイルで用意したインストラクションを埋め込んでいる．
  
  - ボタン1つで表示したり閉じたりできる．
  
    


### 実際の実験時に発行するURLは？
  - oTreeの機能の中で`Rooms`という機能がある．
  - ここにIDを登録することで実行可能．
  - 授業で使う際には学生番号を登録したり．
  - `Sessions`という機能を用いることもできる
      - ランダムな文字列URLが発行されるので，実験の際には`Rooms`の方が使い勝手が良い．



### 下の変な説明がうざめ．

* 実際に実験を行う際には`setting.py`の中で下記のコードを記述して，環境変数の中で	`STUDY`に設定すると良いらしい．
```
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
```
* しかし，あまりに言うことを聞いてくれないので頭に来たから以下のようにしたら動いたので，これで十分．

```
AUTH_LEVEL = 'STUDY'
```



### ホントはデータベースにはこだわりたい．

* oTreeの開発者いわく，容易に動作検証ができるようにデータベースソフトとして`SQLite`を使っているけどあんまりおすすめしないらしい．
* 本番の実験を行う時には`PostgreSQL`を使う方が良いとのこと
    * [We recommend you use PostgreSQL.](https://otree.readthedocs.io/en/latest/server/server-windows.html?highlight=auth_level)
* `settings.py`に以下のコードを書き足したりして使う．
    * もちろん，その前に設定が必要
```
postgres://postgres@localhost/django_db
```

* あわせて`psycopg2`というPythonパッケージが必要になる．

  ```
  pip install -U psycopg2
  ```






### 最近の武器は"intro.js"
* オンライン実験をする際に，インストラクションを読ませるためには様々な工夫が必要
  - 今回は紹介しきれなかったが，結構いける！
  - [intro.js](https://introjs.com/)を使って動的なインストラクションを作成している．
  - 割と悪くない＆oTreeを使った教育的コンテンツの開発には使えるかも．
  - "intro.js"の有無による行動変化をもう少し分析したい．



### もちろん可視化もいける！
* グラフィカルなフィードバックは教育的にも研究的にも興味深い
  - [highcharts](https://www.highcharts.com/)を[XEE](https://xee.jp/)の開発者の林さんに教わってチャレンジ！
  - 今回は紹介しきれなかったが，結構行ける！
  - けど，ギリギリのバグがあったりして死にかけてました．泣



### PGGで変数を2倍じゃなく3倍とか，自由に変えたい．
* いくらでも変えられます．
  - 前もってちょっと手を加えればGUI的に変えられたりします．
- 一番いいのはsetting.pyの**session config**に手を加えるのが一番

<img src="picture/picture1.png" alt="picture1" style="zoom:50%;" />

* `settings.py`での書き方

<img src="picture/picture2.png" alt="picture2" style="zoom:50%;" />

* これだけでなく，アプリ内のプログラムも書き換える必要がある．
  * またどこかの機会でまとめます．



### 動作検証をするのがめんどくさい

* oTreeには`bot`という機能がある．
* この機能を使うと動作検証が容易になる．
  * 今慌てて勉強中です．またどこかの機会でまとめます．
* 本家サイトに細かく説明が書いてある．
  * [コチラ](https://otree.readthedocs.io/en/latest/bots.html)や[コチラ](https://otree.readthedocs.io/en/latest/misc/bots_advanced.html#)



### 途中離脱が起こったらどうしよう？

* クラウドソーシングなどで実験をすると途中離脱がよく発生する．
* 対応策：時間制限を設けて，その時間を超えたらある値が自動的に入力されるようにする．
  * 時間制限の功罪はあれど，今の所それしか手がない．．．？
  * [コチラ](https://otree.readthedocs.io/en/latest/timeouts.html#forms-submitted-by-timeout)などを参考にされると良い．





