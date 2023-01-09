module helloworldfpga( 
input  wire A=0,                                
input  wire B=1,                                
input  wire C=1,                                
input  wire D=0,                                
output  wire a,                                 
output  wire b,                                 
output  wire c,                                 
output  wire d,                                
output  wire e,                                
output  wire f,                                
output  wire g,                                
output  wire G0,                               
output  wire G1,                               
output  wire G2,                               
output  wire G3                                
);                               
always @(*)                                    
begin
G0=(!A&&!C&&D)  (!A&&C&&!D)  (A&&!B&&!C&&D);
G1=(!A&&B&&!C) || (!A&&!B&&C);
G2=(!A&&B) || (A&&!B&&!C);
G3=(A&&!B&&!C);
a=(G0&&!G1&&!G2&&!G3) || (!G0&&!G1&&G2&&!G3);
b=(G0&&!G1&&G2&&!G3)  (!G0&&G1&&G2&&!G3)  (!G0&&!G1&&G2&&G3);
c=(!G0&&G1&&!G2&&!G3) || (!G0&&!G1&&G2&&G3);
d=(!G0&&!G1&&G2&&!G3)  (G0&&G1&&G2&&!G3)  (G0&&!G1&&!G2&&!G3);
e=(G0&&!G2&&!G3)  (!G1&&G2&&!G3)  (G0&&G2&&!G3);
f=(G0&&!G2&&!G3)  (G1&&!G2&&!G3)  (G0&&G1&&!G3);
g=(!G1&&!G2&&!G3) (!G1&&G2&&G3) (G0&&G1&&G2&&!G3);
end   
endmodule
