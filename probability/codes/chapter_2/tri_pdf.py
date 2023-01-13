import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


maxrange=100
maxlim=6.0
x = np.linspace(-1,5,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

#def gauss_pdf(x):
	#return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
#vec_gauss_pdf = scipy.vectorize(gauss_pdf)

def tri_pdf1(x,a,b,c):
	if (x<a):
	 return 0
	 
def tri_pdf2(x,a,b,c):
	if (x>a) and (x<=c):
	 return (2*(x-a))/((b-a)*(c-a))
	 	
def tri_pdf3(x,a,b,c):
	if (x>c) and (x<=b):
	 return (2*(b-x))/((b-a)*(c-a))
	 
def tri_pdf4(x,a,b,c):
	if (x>b):
	 return 0

tri_pdf1 = scipy.vectorize(tri_pdf1)
tri_pdf2 = scipy.vectorize(tri_pdf2)
tri_pdf3 = scipy.vectorize(tri_pdf3)
tri_pdf4 = scipy.vectorize(tri_pdf4)
a=0
b=2
c=1
tri_pdf5=np.piecewise(x,[x<a,((x>=a)&(x<c)),((x>=c)&(x<b)),x>=b],[0,lambda x:(2*(x-a))/((b-a)*(c-a)),lambda x:2*(b-x)/((b-a)*(c-a)),0]) 

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
#plt.plot(x,vec_gauss_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.plot(x,tri_pdf5,label='theoretical')
#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
plt.savefig('/home/admin999/navya/probability/tri_pdf.pdf')
#plt.savefig('../figs/gauss_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
