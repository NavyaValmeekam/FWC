#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}
void other(char *str,int len)
{
int i=0;
FILE *fp;
FILE *fp1;
double x, temp;
double ln(double arg);
fp1=fopen("uni_other.dat","w");
fp = fopen("uni1.dat","r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
	i=i+1;
	temp=-2*log(1-x);
	fprintf(fp1,"%lf\n",temp);
}
fclose(fp);
fclose(fp1);
}
int main(void)
{
 	uniform("uni1.dat",1000000);
	other("uni_other.dat",1000000);
        return 0;
}
