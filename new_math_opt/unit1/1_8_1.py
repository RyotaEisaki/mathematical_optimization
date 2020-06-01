from gurobipy import *

# 分数最適化
# 整数に限らない

model = Model("fractional 1")
x=model.addVar()
y=model.addVar()
z=model.addVar()
t=model.addVar()

model.update()

model.addConstr(x+y+z==32*t)
model.addConstr(2*x+4*y==1)
model.addConstr(2*x+4*y+8*z==80*t)
model.setObjective(x+y,GRB.MINIMIZE)

model.optimize()

print("Opt. Val.", model.ObjVal, ", t=", t.X)
print("(x,y,z)=", x.X/t.X, y.X/t.X, z.X/t.X)