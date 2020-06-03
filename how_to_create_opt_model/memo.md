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
