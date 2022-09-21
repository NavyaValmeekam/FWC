import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          
sys.path.insert(0,'/home/admin999/navya/matrix/CoordGeo')
from line.funcs import *

r1 =3
r2=2.8
r3=4
r4=173
r5=10
r6=3.4
D=np.array(([0,0]))
e1=np.array(([1,0]))
C=5*e1
theta1 = np.pi*2/5
theta2 = np.pi/200
theta3 = np.pi/3.45
A = np.array(([r1*np.cos(theta1),r2*np.sin(theta1)]))
Q = np.array(([r3*np.cos(theta2),-(r4*np.sin(theta2))]))
B = np.array(([r5*np.cos(theta3),r6*np.sin(theta3)]))
P = (D+C)/2
#print(A)
#print(B)
#print(C)
#print(D)
#print(P)
#print(Q)
#H1 = np.array(([4,0]))


v1=P-B
v2=P-C
ar_t1=0.5*np.linalg.norm((np.cross(v1,v2)))

v3=D-P
v4=Q-P
ar_t2=0.5*np.linalg.norm((np.cross(v3,v4)))
BPC='{0:.2g}'.format(ar_t1)
DPQ='{0:.2g}'.format(ar_t2)

print("Ar(BPC)=",BPC)
print("Ar(DPQ)=",DPQ)
if(BPC==DPQ):
    print("area of triangle BPC is equal to area of triangle DPQ")
else : print("area of triangle BPC is not equal to area of triangle DPQ")
x_DC = line_gen(D,C)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_QC = line_gen(Q,C)
x_DQ = line_gen(D,Q)
x_CB = line_gen(C,B)
x_AB = line_gen(A,B)
x_AQ = line_gen(A,Q)
x_BP = line_gen(B,P)
#x_BH1= line_gen(B,H1)

plt.plot(x_DC[0,:],x_DC[1,:])#,label='$Line')
plt.plot(x_DA[0,:],x_DA[1,:])#,label='$Line')
plt.plot(x_AC[0,:],x_AC[1,:])#,label='$Line')
plt.plot(x_QC[0,:],x_QC[1,:])#,label='$Line')
plt.plot(x_DQ[0,:],x_DQ[1,:])#,label='$Line')
plt.plot(x_CB[0,:],x_CB[1,:])#,label='$Line')
plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Line')
plt.plot(x_AQ[0,:],x_AQ[1,:])#,label='$Line')
plt.plot(x_BP[0,:],x_BP[1,:])#,label='$Line')
#plt.plot(x_BH1[0,:],x_BH1[1,:])#,label='$Line')

tri_coords = np.vstack((A,C,D,Q,B,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','C','D','Q','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal') 
plt.savefig('/home/admin999/navya/matrix/line.pdf')
plt.show()
