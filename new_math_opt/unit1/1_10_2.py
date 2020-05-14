from gurobipy import *

# 実行不可能な問題

# food, cost, 栄養素の量
F, c, d = multidict({
    "OQPounder": [360,{"Cal":556,"Carbo":39,"Protein":30,"VitA":147,"VitC":10,"Calc":221,"Iron":2.4}],
    "Big M":[320,{"Cal":556,"Carbo":46,"Protein":26,"VitA":97,"VitC":9,"Calc":142,"Iron":2.4}],
    "FFilet":[270,{"Cal":356,"Carbo":42,"Protein":14,"VitA":28,"VitC":1,"Calc":76,"Iron":0.7}],
    "Chicken":[290,{"Cal":431,"Carbo":45,"Protein":20,"VitA":9,"VitC":2,"Calc":37,"Iron":0.9}],
    "Fries":[190,{"Cal":249,"Carbo":30,"Protein":3,"VitA":0,"VitC":5,"Calc":7,"Iron":0.6}],
    "Milk":[170,{"Cal":138,"Carbo":10,"Protein":7,"VitA":80,"VitC":2,"Calc":227,"Iron":0}],
    "VegJuice":[100,{"Cal":69,"Carbo":17,"Protein":1,"VitA":750,"VitC":2,"Calc":18,"Iron":0}],
})
# print(c["Chicken"]["Iron"])

# 加減と上限
N,a,b=multidict({
    "Cal": [2000,3000],
    "Carbo": [300,375],
    "Protein": [50,60],
    "VitA": [500,750],
    "VitC": [85,100],
    "Calc": [660,900],
    "Iron": [6.0,7.5]
})

# print(a["Cal"])

model=Model("modern diet")
# 変数
x={}
for j in F:
    x[j]=model.addVar(vtype="I","x(%s)"%i)
model.update()
for i in N:
    model.addConstr(quicksum(d[j][i]*x[j] for j in F) >= a[i], "NutrLB(%s)"%i)
    model.addConstr(quicksum(d[j][i]*x[j] for j in F) <= b[i], "NutrUB(%s)"%i)
model.setObjective(quicksum(c[j]*x[j] for j in F), GRB.MINIMIZE)

# ここまでで、最適化を行うと実行不可能であることがわかる
# 既約不整合部分系：実行不可能になっている原因の制約と変数から構成

model.computeIIS()
for c in model.getConstrs():
    if c.IISConstr:
        print(c.ConstrName)
        