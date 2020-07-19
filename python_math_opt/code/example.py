import numpy as np
import revised_simplex
from revised_simplex import lp_RevisedSimplex

A=np.array([[2,2,-1],[2,-2,3],[0,2,-1]])
c=np.array([4,3,5])
b=np.array([6,8,4])

lp_RevisedSimplex(c,A,b)