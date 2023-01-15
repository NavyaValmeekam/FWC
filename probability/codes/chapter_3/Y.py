import numpy as np
import matplotlib.pyplot as plt
len=10000
count1=0
count2=0

x=2*np.random.randint(2, size=len)-1
for i in range(0,len):
    if(x[i] == 1):
        count1=count1+1
    elif(x[i] == -1):
        count2=count2+1
prob1=count1/len
print(prob1)
prob2=count2/len
print(prob2)

N= np.random.normal(0,1,len)
A=5
Y=A*x+N


    
