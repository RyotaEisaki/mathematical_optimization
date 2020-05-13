from gurobipy import *

model = Model("lo1")

# 変数の定義
x1 = model.addVar(vtype="C", name="x1")
x2 = model.addVar(name="x2")
x3 = model.addVar(ub=30,name="x3")

model.update()

# 制約
model.addConstr(2*x1+x2+x3<= 60)
#別の書き方
# L1 = LinExpr([2,1,1]),[x1,x2,x3]
# model.addConstr(L1,"<",60)
# 別の書き方
# model.addConstr(lhs=L1,sense="<",rhs=60)

model.addConstr(x1+2*x2+x3<= 60)

# 目的関数
# 目的関数の方向を省略する場合
# model.ModelSense=-1 #最小化＋1が規定値

model.setObjective(15*x1+18*x2+30*x3,GRB.MAXIMIZE)

# 最適化
model.optimize()

# 目的関数値の出力
print("Opt. Value=", model.ObjVal)

# 最適解の出力
for v in model.getVars():
    print(v.VarName, v.X)

