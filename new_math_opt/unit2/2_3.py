from gurobipy import *

# k-メディアン問題
# メディアン問題
# 小火薬から最も近い施設への距離の「合計」を最小にするようにグラフ内の点から決められた数の施設を選択せよ

def kmedian(I,J,c,k):
    model=Model("k-median")
    x, y={},{}
    for j in J:
        y[j]=model.addVar(vtype="B")
        for i in I:
            x[i,j]=model.addVar(vtype="B")
    model.update()
    for i in I:
        model.Constr(quicksum(x[i,j] for j in J)== 1)
        for j in J:
            model.addConstr(x[i,j] <= y[j])
    model.addConstr(quicksum(y[j] for j in J) ==k)
    model.setObjective(quicksum(x[i,j]*x[i,j] for i in I for j in J), GRB.MINIMIZE)
    model.update()
    model.__data=x,y
    return model