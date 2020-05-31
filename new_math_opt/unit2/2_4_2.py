from gurobipy import *

def k_cover(I,J,c,k):
    model=Model("k-center")
    z,y,x={},{},{}
    for i in I:
        z[i]=model.addVar(vtype="B")
    for j in J:
        y[j]=model.addVar(vtype="B")
        for i in I:
            z[i,j]=model.addVar(vtype="B")
    model.update()
    for i in I:
        model.addConstr(quicksum(x[i,j] for j in J)+z[i]=1)
        for j in J:
            model.addConstr(x[i,j]<=y[j])
    model.addConstr(quicksum(y[j] for j in J)==k)
    model.setObjective(quicksum(z[i] for i in I), GRB.MINIMIZE)
    model.update()
    model.__data=x,y,z
    return model