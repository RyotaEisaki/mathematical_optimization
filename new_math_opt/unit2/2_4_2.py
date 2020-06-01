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
def solve_kcenter(I,J,c,k):
    model=k_cover(I,J,c,k)
    model.Params.Cntoff=.1 # 探索の途中で下界が0.1を超えたら終了するように設定している
    x,y,z=model.__data
    LB=0
    UB=max(c[i,j], for (i,j) in c)
    while UB-LB > 1.e-4:
        theta=(UB-LB)/2
        for j in J:
            for i in I:
                if c[i,j]>theta:
                    x[i,j].UB=0
                else:
                    x[i,j].UB=1.0
        model.updata()
        model.optimize()
        infeasibility=sum([z[i].X for i in I])
        if infeasibility>0:
            LB=theta
        else:
            UB=theta