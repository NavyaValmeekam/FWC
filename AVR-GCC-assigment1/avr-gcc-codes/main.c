//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>
#include<stdbool.h>
 
int main (void)
{
		
	 bool A=1,B=0,C=0,D=0;
	 bool G0,G1,G2,G3,a,b,c,d,e,f,g;

	   DDRD   = 0xFC;
	   DDRB   = ((1 << DDB0));
	        
           //Equations
	   

  G0=((!A&&!C&&D) || (!A&&C&&!D) || (A&&!B&&!C&&D));
  G1=((!A&&B&&!C) || (!A&&!B&&C));
  G2=((!A&&B) || (A&&!B&&!C));
  G3=((A&&!B&&!C));
  a=((G0&&!G1&&!G2&&!G3) || (!G0&&!G1&&G2&&!G3));
  b=((G0&&!G1&&G2&&!G3) || (!G0&&G1&&G2&&!G3) || (!G0&&!G1&&G2&&G3));
  c=((!G0&&G1&&!G2&&!G3) || (!G0&&!G1&&G2&&G3));
  d=((!G0&&!G1&&G2&&!G3) || (G0&&G1&&G2&&!G3) || (G0&&!G1&&!G2&&!G3));
  e=((G0&&!G2&&!G3) || (!G1&&G2&&!G3) || (G0&&G2&&!G3));
  f=((G0&&!G2&&!G3) || (G1&&!G2&&!G3) || (G0&&G1&&!G3));
  g=((!G1&&!G2&&!G3) || (!G1&&G2&&G3) || (G0&&G1&&G2&&!G3));

	   PORTD |=(a << 2);
	   PORTD |=(b << 3);
	   PORTD |=(c << 4);
	   PORTD |=(d << 5);
	   PORTD |=(e << 6);
	   PORTD |=(f << 7);
	   PORTB |=(g << 0);

           
   			   
	   return 0;
 }	       	  							    

  	  							 
