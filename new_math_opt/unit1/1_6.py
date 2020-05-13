from gurobipy import *

# 多品種輸送問題

# 製造可能な製品
produce={1:[2,4],2:[1,2,3],3:[2,3,4]}

# 各顧客の各製品に対する需要量
d={
    (1,1):80, (1,2):85, (1,3):300, (1,4):6,
    (2,1):270, (2,2):160, (2,3):400, (2,4):7,
    (3,1):250, (3,2):130, (3,3):350, (3,4):4,
    (4,1):160, (4,2):60, (4,3):200, (4,4):3,
    (5,1):180, (5,2):40, (5,3):150, (5,4):5
}

# consumer
I=[1,2,3,4,5]

# manufacture capacity
J,M=multidict({1:3000,2:3000,3:3000})

# weight
K, weight =multidict({1:5,2:2, 3:3, 4:4})

# cost
cost={
    (1,1):4, (1,2):6, (1,3):9, 
    (2,1):5, (2,2):4, (2,3):7, 
    (3,1):6, (3,2):3, (3,3):4, 
    (4,1):8, (4,2):5, (4,3):3, 
    (5,1):10, (5,2):8, (5,3):4
}

# calc cost
c={}
for i in I:
    for j in J:
        for k in produce[j]:
            c[i,j,k]=cost[i,j] * weight[k]

# difinition
model = Model("multi-commodity transportation")
x={}
for i,j,k in c:
    x[i,j,k]=model.addVar(vtype="C")

model.update()

# constraction
# demand
for i in I:
    for k in K:
        model.addConstr(quicksum(x[i,j,k] for j in J if (i,j,k) in x) == d[i,k])
# capacity
for j in J:
    model.addConstr(quicksum(x[i,j,k] for (i,j2,k) in x if j2==j)<=M[j])

# object
model.setObjective(quicksum(c[i,j,k]*x[i,j,k] for (i,j,k) in x), GRB.MINIMIZE)

model.optimize()
print("Optimal value:", model.ObjVal)
