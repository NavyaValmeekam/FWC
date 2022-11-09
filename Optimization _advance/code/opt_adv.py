import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                  
sys.path.insert(0,'/sdcard/Download/Matrix/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

def f(x,a,b,c):
    return a*x**2+b*x+c

def df(x):
    return 2*a*x+b

def g(y,l,m,n):
    return l*y**2+m*y+n

def dg(y):
    return 2*l*y+m

a = 3
b = -24
c = 70
l = 3
m = -12
n = 70


#Coordinate x using gradient descent
cur_x = 1
alpha = 0.001
precision = 0.000000001
previous_step_size = 1
max_iters = 1000000
iters = 1000

#Gradient descent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x            
    cur_x -= alpha * df(prev_x)  
    previous_step_size = abs(cur_x - prev_x)  
    iters+=1  

min_val = f(cur_x,a,b,c)
#print("<Minimum value of f(x) is", min_val, "at","x =",cur_x)

#Coordinate y using gradient descent
cur_y = 1
beta = 0.001
precisions = 0.000000001
previous_step_sizes = 1
max_iters = 1000000
iterss = 1000

#Gradient descent calculation
cur_y = 1
while (previous_step_sizes > precisions) & (iterss < max_iters) :
    prev_y = cur_y            
    cur_y -= beta * dg(prev_y)  
    previous_step_sizes = abs(cur_y - prev_y)  
    iterss+=1  

minval = g(cur_y,l,m,n)
#print("<Minimum value of f(y) is", minval, "at","y =",cur_y)
print("Minima of f(x,y) is","(",cur_x,cur_y,")")

A=np.array(([2,1]))
B=np.array(([6,2]))
C=np.array(([4,3]))
x_AC = line_gen(A,C)
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
P=(A+B+C)/3

plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Line')
plt.plot(x_AC[0,:],x_AC[1,:])#,label='$Line')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Line')


tri_coords = np.vstack((A,C,B,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','C','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/sdcard/Download/Matrix/Optimization_adv/opt_adv.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/Matrix/Optimization_adv/opt_adv.pdf' "))
plt.show()
