from gurobipy import *

# 切断問題

def CuttingStockExample():
    B=9 # 厚紙のサイズ
    w=[2,3,4,5,6,7,8] # 各注文の幅
    q=[4,2,6,6,2,2,2] # 注文数
    s=[] # アイテムのサイズのリスト 
    for j in range(len(w)):
        for i in range(q[j]):
            s.append(w[j])
    return s,B

# First Decreasing: FFD 
# サイズの大きいアイテムを順番に開いている瓶に入れる方法
def FFD(s,B):
    remain=[B] # 現在使える人の残りサイズ
    sol=[[]] # 解を保管するリスト
    for item in sorted(s,reverse=True): # アイテムのサイズを大きい順に取り出している
        for (j,free) in enumerate(remain):
            if free >= item:
                remain[j]-=item
                sol[j].append(item)
                break
            else:
                sol.append([item])
                remain.append(B-item)
    return sol

def bpp(s,B):
    n=len(s)
    U=len(FFD(s,B))
    model=Model("bpp")
    x,y={}, {}
    for i in range(n):
        for j in range(U):
            x[i,j]=model.addVar(vtype="B")
    for j in range(U):
        y[j]=model.addVar(vtype="B")
    model.update()
    for i in range(n):
        model.addConstr(quicksum(x[i,j] for j in range(U)) ==1)
    for j in range(U):
        model.addConstr(quicksum([i]*x[i,j] for i in range(n))<+B*y[i])
    for j in range(U):
        for i in range(n):
            model.addConstr(x[i,j]<=y[j])
    model.setObjective(quicksum(y[j] for j in range(U)), GRB.MINIMIZE)
    model.update()
    model.__data=x,y
    return model

# メイン関数
if __name__=="__main__":
    x,y={},{}
    s,B= CuttingStockExample()
    sol=FFD(s,B)
    model=bpp(s,B)
    model.optimize()
   
