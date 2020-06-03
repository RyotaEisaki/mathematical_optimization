### ライプラリのインポート
from pulp import LpProblem, LpMaximize, LpVariable, value
### 数理モデルの作成
- 最大化
m=LpProblem(sense=LpMaximize)
- 最小化
m=LpProblem()
### 変数の作成
- 連続変数(自由変数)
x=LpVariable(name)
- 0-1変数
x=LpVariable(name, cat=LpBinary)
- 連続変数のリスト
x=[LpVariable(name_i, lowBound=0) for i in range(n)]
- 0-1変数のリスト
x=[LpVariable(name_i, cat=LpBinary) for i in range(n)]
### 目的関数の設定
m += 「式」
m.objective で設定した目的関数を参照できる
### 制約条件の追加
m += 「式」 == 「式」

m += 「式」 <= 「式」

m += 「式」 >= 「式」

式には変数の合計、係数と変数の内積を書くことが多い

from pulp import lpDot, lpSum

lpSum(変数のリスト)　# 和の書き方

lpDot(係数のリスト、変数のリスト) # 内積の書き方

### ソルバーの実行
m.solve()

ソルバーを実行した結果のステータス

from pulp import LpStatus

m.status # 実行した結果の整数値

LpStatus[m.status] # 実行した血kの文字列

- CBCを利用(デフォルト)
m.solve()
- GUROBIを利用
m.solve(GUROBI_CMP())
- CPLEXを利用
m.solve(CPLEX_CMP())
- GLPKを利用
m.solve(GLPK_CMP())
- CBCでオプションを指定
cmd=PULP_CBC_CMD(maxSecond=1,fracGap=0.01, keepFiles=True)

m.solve(cmd)

- - maxSeconde: 打ち切り時間を秒で指定する。この指定時間を超えたきりのいいところで打ち切り。途中解があれば出力
- - fracGap: 解の良さの指標MIP gap を指定する。