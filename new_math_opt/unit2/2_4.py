from gurobipy import *

# k-センター問題
# センター問題
# 酷悪から最も近い施設への距離の「最大値」を最小にするようにグラフないの点から決められた加増の施設を選択する
# 最大値の最小化　通常の数理最適化ソルバーが苦手とするタイプの目的関数

def kcenter(I,J,c,k):
    model=Model('k-center')
    z=model.addVar(vtype="C")
    x,y={},{}
    for j in J:
        y[j]=model.addVar(vtype="B")
        for i in I:
            x[i,j]=model.addVar(vtype="B")
    model.update()
    for i in I:
        model.addConstr(quicksum(x[i,j] for j in J)==1)
        for j in J:
            model.addConstr(x[i,j]<=y[j])
            model.addConstr(c[i,j]*x[i,j]==k)
    model.addConstr(quicksum(y[j] for j in J)==k)
    model.setObjective(z, GRB.MINIMIZE)
    model.update()
    model.__data=x,y
    return model