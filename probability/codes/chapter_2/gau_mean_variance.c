#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void gaussian(char *str, int len)
{
int i,j;
double temp2;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp2 = 0;
for (j = 0; j < 12; j++)
{
temp2 += (double)rand()/RAND_MAX;
}
temp2-=6;
fprintf(fp,"%lf\n",temp2);
}
fclose(fp);

}

//mean

double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen("gau.dat","r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;
}


//variance
double variance(char *str)
{
int i=0,c,j=0;
FILE *fp;
double x,temp1=0.0,temp=0,var=0.0,x1;

fp = fopen("gau.dat","r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp=temp+x;
}
fclose(fp);
temp=temp/(i-1);
fp = fopen("gau.dat","r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
j=j+1;
//Add all numbers in file
x1=x-temp;
temp1=temp1+x1*x1;
}
fclose(fp);
var=temp1/(i-1);
return var;

}

int main(void)
{
 	gaussian("gau.dat",1000000);
	printf("%f",mean("gau.dat"));
	printf("\n");
	printf("%f",variance("gau.dat"));
        return 0;
}
