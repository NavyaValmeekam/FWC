import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                  
sys.path.insert(0,'/home/admin999/navya/matrix/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if


A = np.array([[1,1],[3,2]])
B=np.array([[1,0],[0,1]])
A_b1 = np.array([20,48]).reshape(2,1)
A_b2 = np.array([0,0]).reshape(2,1)
# objective function coeffs
c = np.array([22, 18])
x = cp.Variable((2,1))
#profit function
p = c@x
obj = cp.Maximize(p)
#Constraints
constraint = [ A@x <= A_b1, B@x >= A_b2] 
#solution
prob = cp.Problem(obj, constraint)
prob.solve()
#print("status:", prob.status)
print("optimal value:", np.round_(p.value))
print("optimal var:", np.round_(x.value))

x1=np.linspace(0,45,150)
#print(len(x1))
y1=(20-x1)
y2=(48-3*x1)/2
plt.plot(x1,y1,label='x+y=20')
plt.plot(x1,y2,label='3x+2y=48')
y4=np.zeros(len(x1))
plt.plot(x1,y4,label='y=0')
plt.plot(y4,x1,label='x=0')
plt.title('')
plt.ylim([-2,30])
# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/home/admin999/navya/matrix/conics/conics.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/Download/anusha1/python1/opt1.pdf"))
plt.show()
