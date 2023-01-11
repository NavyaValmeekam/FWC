import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#Sample size
simlen = 10000
#Possible outcomes
n = range(2,13)
# Generate X1 and X2
y = np.random.randint(1,7, size=(2, simlen))

#Generate X
X = np.sum(y, axis = 0) 
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen
#Theoretical probability
n1 = range(2,8)
n2 = range(8,13)
panal1 = (n1 -np.ones((1,6)))
panal2 = (13*np.ones((1,5))-n2)
panal = np.concatenate((panal1,panal2),axis=None)/36

#convolution
for n1 in range(2,13):
    P_px=0
    if((n1>=2) & (n1<=7)):
        P_px=(n1-1)/36
    elif((n1>=8) & (n1<=12)):
        P_px=(13-n1)/36
    elif((n1>12)):
        P_px=0
    print(P_px)

#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor

#If using termux
plt.savefig('/home/admin999/navya/probability/dice.pdf')
#plt.savefig('figs/pmf.png')
#subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
#else
plt.show()
