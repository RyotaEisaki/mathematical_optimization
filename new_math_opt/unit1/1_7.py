from gurobipy import *

# 混合問題

# 成分比率
a={
    (1,1):.25, (1,2):.15, (1,3):.30,
    (2,1):.3, (2,2):.30, (2,3):.10,
    (3,1):.15, (3,2):.65, (3,3):.05,
    (4,1):.10, (4,2):.05, (4,3):.85
}

# price
I,p=multidict({1:5, 2:6, 3:8, 4:20})
# lb and ub
K, LB, UB =multidict({1:[.1,.2], 2:[.0,.35], 3:[.45,1.0]})

# difine
model=Model("product mix")
x={}
for i in I:
    x[i]=model.addVar()
model.update()

# constration
model.addConstr(quicksum(x[i] for i in I) ==1)
for k in K:
    model.addConstr(quicksum(a[i,k]*x[i] for i in I) <= UB[k])
    model.addConstr(quicksum(a[i,k]*x[i] for i in I) >= LB[k])

# object
model.setObjective(quicksum(p[i]*x[i] for i in I), GRB.MINIMIZE)

# optimization
model.optimize()

# print result
for i in I:
    print(i,x[i].X)