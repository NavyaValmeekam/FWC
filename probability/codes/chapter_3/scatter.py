import numpy as np
import matplotlib.pyplot as plt
length=10000
count1=0
count2=0

mean = [0, 0]
covariance = [[1, 0], [0, 1]]

x=2*np.random.randint(2, size=length)-1
for i in range(0,length):
    if(x[i] == 1):
        count1=count1+1
    elif(x[i] == -1):
        count2=count2+1
prob1=count1/length
print(prob1)
prob2=count2/length
print(prob2)

n1,n2= np.random.multivariate_normal(mean,covariance,length).T
A1=5
A=10**(0.1*A1)
Y=A*x+n2
x1=np.linspace(-10,10,len(Y))
plt.scatter(x1,Y,color='red')
plt.xlabel("$x$")
plt.ylabel("$Y$")
plt.savefig('Y_scatter.pdf')
plt.show()


    
