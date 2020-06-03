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
#### 
