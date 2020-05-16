from gurobipy import *

# 容量制限付き施設配置問題

# データの定義
def make_data():
    # 顧客、需要量
    I,d=multidict({1:80, 2:270, 3:250, 4:160, 5:180})
    # 工場、容量、解説費用
    J, M, f=multidict({1:[500, 1000], 2:[500,1000], 3:[500,1000]})
    # 工場から顧客までの輸送費用
    c={
        (1,1):4, (1,2):6, (1,3):9,
        (2,1):5, (2,2):4, (2,3):7,
        (3,1):6, (3,2):3, (3,3):4,
        (4,1):8, (4,2):5, (4,3):3,
        (5,1):10, (5,2):8, (5,3):4,
    }
    return I,J,d,M,f,c


# 施設配置問題のモデル
def flp(I,J,d,M,f,c):
    model=Model("flp")
    x,y={},{}
    for j in J:
        y[j]=model.addVar(vtype="B")
        for i in I:
            x[i,j]=model.addVar(vtype="C")
    model.update()
    for i in I:
        model.addConstr(quicksum(x[i,j] for j in J)==d[i])
    for j in J:
        model.addConstr(quicksum(x[i,j] for i in I) <= M[j]*y[j])
    for (i,j) in x:
        model.addConstr(x[i,j] <= d[i]*y[j])
    model.setObjective(
        quicksum(f[j]*y[j] for j in J) + quicksum(c[i,j]*x[i,j] for i in I for j in J), GRB.MINIMIZE 
    )
    model.__data=x,y
    return model

# メイン関数
if __name__=="__main__":
    I, J, d,c,f,M = make_data()
    model=flp(I,J,d,c,f,M)
    # x={}
    model.optimize()
    print("Optimal value:", model.ObjVal)
    print(model.data)
    EPS=1.e-6
    for (i,j) in x:
        if x[i,j].X >EPS:
            print("sending quantity %10s from factory %3s to customer %3s"%(x[i,j].X,j,i))

