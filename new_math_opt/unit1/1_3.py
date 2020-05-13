from gurobipy import *

#整数最適化問題

model=Model("puzzle")

x=model.addVar(vtype="I")
y=model.addVar(vtype="I")
z=model.addVar(vtype="I")

model.update()

model.addConstr(x+y+z ==32)
model.addConstr(2*x+4*y+8*z==80)

model.setObjective(y+z,GRB.MINIMIZE)

model.optimize()
print("Opt. Val.=", model.ObjVal)
print("(x,y,z)=", x.X, y.X, z.X)