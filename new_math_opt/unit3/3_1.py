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
    remain=[B]
    sol=[[]]
    for item in sorted(s,recerse=True):
        for (j,free) in emumerate(remain):
            if free >= item:
                remain[j]-=item
                sol[j].append(item)
                break