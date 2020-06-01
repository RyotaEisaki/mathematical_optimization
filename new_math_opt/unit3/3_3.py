from gurobipy import *

# 切断問題に対する列生成

# 全ての初期切断パターンを含んだリストtを作成する
B=9 # 厚紙のサイズ
w=[2,3,4,5,6,7,8] # 各注文の幅
t=[]
m=len(w)
for i in range(m):
    width=w[i]
    pat=[0]*m
    pat[i]=int(B/width)
    t.append(pat)
print(t)

# モデリングのコツ
# 変数の数が非常に多いときは時には列生成方を使う