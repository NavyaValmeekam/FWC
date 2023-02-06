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
void uniform3(char *str, int len)
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
void uniform4(char *str, int len)
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
void normalRandom1(char *str,int len) {
int i=0;
FILE *fp;
FILE *fp1;
FILE *fp2;
double v1,v2,norm1;
fp=fopen("normal1.dat","w");
fp1=fopen("uni1.dat","r");
fp2=fopen("uni2.dat","r");
while((fscanf(fp1,"%lf",&v1)!=EOF) && (fscanf(fp2,"%lf",&v2)!=EOF))
{
	i=i+1;
	norm1= cos(2*3.14*v2)*sqrt(-2.*log(v1));
	fprintf(fp,"%lf\n",norm1);
}
fclose(fp2);
fclose(fp1);
fclose(fp);
}
void normalRandom2(char *str,int len) {
int i=0;
FILE *fp;
FILE *fp1;
FILE *fp2;
double v3,v4,norm2;
fp=fopen("normal2.dat","w");
fp1=fopen("uni3.dat","r");
fp2=fopen("uni4.dat","r");
while((fscanf(fp1,"%lf",&v3)!=EOF) && (fscanf(fp2,"%lf",&v4)!=EOF))
{
	i=i+1;
	norm2= cos(2*3.14*v4)*sqrt(-2.*log(v3));
	fprintf(fp,"%lf\n",norm2);
}
fclose(fp2);
fclose(fp1);
fclose(fp);
}
void V(char *str,int len){
int i=0;
FILE *fp;
FILE *fp1;
FILE *fp2;
double x1,x2,V;
fp=fopen("V.dat","w");
fp1=fopen("normal1.dat","r");
fp2=fopen("normal2.dat","r");
while((fscanf(fp1,"%lf",&x1)!=EOF) && (fscanf(fp2,"%lf",&x2)!=EOF))
{
	i=i+1;
	V= x1*x1+x2*x2;
	fprintf(fp,"%lf\n",V);
}
fclose(fp2);
fclose(fp1);
fclose(fp);
}
int main(void)
{
 	uniform1("uni1.dat",1000000);
	uniform2("uni2.dat",1000000);
	uniform3("uni3.dat",1000000);
	uniform4("uni4.dat",1000000);
	normalRandom1("normal1.dat",1000000);
	normalRandom2("normal2.dat",1000000);
	V("V.dat",1000000);
        return 0;
}
