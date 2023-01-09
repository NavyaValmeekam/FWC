//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "Galaxy A30s42EC"  // Replace with your network credentials
#define STAPSK  "navya123"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;
int A,B,C,D,G0,G1,G2,G3;

void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

void setup(){
  OTAsetup();

  //-------------------//
  // Custom setup code //
  //-------------------//
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);  
  pinMode(4, OUTPUT);  
  pinMode(5, OUTPUT);  
  pinMode(6, OUTPUT);  
  pinMode(7, OUTPUT);  
  pinMode(8, OUTPUT);  
}

void loop() {
  OTAloop();
  delay(10);  // If no custom loop code ensure to have a delay in loop
  //-------------------//
  // Custom loop code  //
  //-------------------//
  //U=digitalRead(2);
  //V=digitalRead(4);
  //W=digitalRead(6);
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
  
  digitalWrite(2, a); //LSB
  digitalWrite(3, b);
  digitalWrite(4, c);
  digitalWrite(5, d);
  digitalWrite(6, e);
  digitalWrite(7, f);
  digitalWrite(8, g);

}
