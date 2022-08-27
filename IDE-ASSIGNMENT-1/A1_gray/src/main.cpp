
#include <Arduino.h>
int A=1,B=0,C=0,D=1;
int G0,G1,G2,G3;
int a,b,c,d,e,f,g;

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int a,int b,int c,int d,int e,int f,int g)
{
  digitalWrite(2, a); //LSB
  digitalWrite(3, b); 
  digitalWrite(4, c); 
  digitalWrite(5, d);
  digitalWrite(6, e);
  digitalWrite(7, f);
  digitalWrite(8, g);

}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  G0=(!A&&!C&&D) || (!A&&C&&!D) || (A&&!B&&!C&&D);
  G1=(!A&&B&&!C) || (!A&&!B&&C);
  G2=(!A&&B) || (A&&!B&&!C);
  G3=(A&&!B&&!C);
  a=(G0&&!G1&&!G2&&!G3) || (!G0&&!G1&&G2&&!G3);
  b=(G0&&!G1&&G2&&!G3) || (!G0&&G1&&G2&&!G3) || (!G0&&!G1&&G2&&G3);
  c=(!G0&&G1&&!G2&&!G3) || (!G0&&!G1&&G2&&G3);
  d=(!G0&&!G1&&G2&&!G3) || (G0&&G1&&G2&&!G3) || (G0&&!G1&&!G2&&!G3);
  e=(G0&&!G2&&!G3) || (!G1&&G2&&!G3) || (G0&&G2&&!G3);
  f=(G0&&!G2&&!G3) || (G1&&!G2&&!G3) || (G0&&G1&&!G3);
  g=(!G1&&!G2&&!G3) || (!G1&&G2&&G3) || (G0&&G1&&G2&&!G3);
  
disp_7447(a,b,c,d,e,f,g);  
}

