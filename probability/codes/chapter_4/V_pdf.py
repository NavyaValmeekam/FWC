import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


maxrange=50
maxlim=10.0
x = np.linspace(0,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('tri.dat',dtype='double')
randvar = np.loadtxt('V.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list


	 	 	
#tri_pdf11 = scipy.vectorize(tri_pdf1)

plt.plot(x[0:(maxrange-1)].T,pdf,'--',color='black')
#plt.plot(x,tri_pdf12(x,0,2,1),'*')#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical"])

#if using termux
#plt.savefig('figs/cdf/uni_pdf.pdf')
#plt.savefig('figs/cdf/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open figs/cdf/uni_pdf.pdf"))
plt.savefig('tri_pdf1.pdf')
#plt.savefig('figs/clt/gauss_pdf.eps')
#subprocess.run(shlex.split("termux-open figs/clt/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
