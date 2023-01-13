#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void uniform1(char *str, int len)
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
void uniform2(char *str, int len)
{
int i;
FILE *fp;

fp=fopen(str,"w");
for(i=0;i<len;i++)
{
	fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);
}
void triangular(char *str,int len)
{
int i=0;
FILE *fp;
FILE *fp1;
FILE *fp2;
double x, t,x1;
fp=fopen("tri.dat","w");
fp1 = fopen("uni1.dat","r");
fp2=fopen("uni2.dat","r");
//get numbers from file
while((fscanf(fp1,"%lf",&x)!=EOF) && (fscanf(fp2,"%lf",&x1)!=EOF)) 
{
	i=i+1;
	t=x+x1;
	fprintf(fp,"%lf\n",t);
}
fclose(fp2);
fclose(fp1);
fclose(fp);
}
int main(void)
{
 	uniform1("uni1.dat",1000000);
	uniform2("uni2.dat",1000000);
	triangular("tri.dat",1000000);
        return 0;
}
