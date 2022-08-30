.include "/home/navya/navya1/m328Pdef.inc"

ldi r30, 0b11111100 ;identifying output pins 2,3,4,5
out DDRD,r30
ldi r30, 0b00000001
out DDRB,r30
ldi r31,0b11000011
out DDRB,r31
ldi r31,0b11100111
out PORTB,r31

ldi r17,0b00000001
ldi r18,0b00000001
ldi r19,0b00000001
ldi r20,0b00000001

LSR r31
LSR r31 

AND r17,r31          ;r17=D
LSR  r31
AND r18,r31           ;r18=C
LSR r31
AND r19,r31           ;r19=B
LSR r31
AND r20,r31           ;r20=A

ldi r21,0b00000001	
eor r21,r17           ;r21=D'

ldi r22,0b00000001
eor r22,r18           ;r22=C'

ldi r23,0b00000001
eor r23,r19           ;r23=B'

ldi r24,0b00000001
eor r24,r20           ;r24=A'


mov r0,r22                    
AND r0,r17
mov r11,r21
AND r11,r18
OR r0,r11             ;G0=C'D+D'C (A)
mov r1,r23
AND r1,r18
mov r12,r22
AND r12,r19
OR r1,r12            ;G1=B'C+C'B (B)
mov r2,r19
OR r2,r20             ;G2=A+B     (C)
mov r3,r20            ;G3=A       (D)

ldi r25,0b00000001
eor r25,r0            ;r25=G0'
ldi r26,0b00000001
eor r26,r1            ;r26=G1'
ldi r27,0b00000001
eor r27,r2            ;r27=G2'
ldi r28,0b00000001
eor r28,r3            ;r28=G3'

mov r4,r0
AND r4,r26
AND r4,r27
mov r5,r25
AND r5,r26
AND r5,r2
AND r5,r28
OR r4,r5             ;a=G0G1'G2'+G0'G1'G2G3'

mov r5,r25
AND r5,r3
mov r6,r25
AND r6,r1
AND r6,r2
mov r7,r0
AND r7,r26
AND r7,r2
AND r7,r28
OR r5,r6
OR r5,r7            ;b=G0'G3+G0'G1G2+G0G1'G2G3'

mov r6,r25
AND r6,r3
mov r7,r25
AND r7,r1
AND r7,r27
OR r6,r7           ;c=G0'G3+G0'G1G2'

mov r7,r0
AND r7,r26
AND r7,r27
mov r8,r0
AND r8,r1
AND r8,r2
mov  r9,r25
AND r9,r26
AND r9,r2
AND r9,r28
OR r7,r8
OR r7,r9           ;d=G0G1'G2'+G0G1G2+G0'G1'G2G3'

mov r8,r0
AND r8,r1
mov r9,r0
AND r9,r27
mov r10,r26
AND r10,r2
AND r10,r28
OR r8,r9
OR r8,r10         ;e=G0G1+G0G2'+G1'G2G3'

mov r9,r0
AND r9,r1
mov r10,r0
AND r10,r27
mov r11,r1
AND r11,r27
OR r9,r10
OR r9,r11         ;f=G0G1+G0G2'+G1G2'

mov r10,r3
mov r11,r26
AND r11,r27
mov r12,r0
AND r12,r1
AND r12,r2
OR r10,r11
OR r10,r12       ;g=G3+G1'G2'+G0G1G2


mov r30,r4            ;r30=0000000a
LSL r30               ;r30=000000A0
OR r30,r5            ;r30=000000ab
LSL r30               ;r30=00000ab0
OR r30,r6            ;r30=00000abc
LSL r30               ;r30=0000abc0
OR r30,r7            ;r30=0000abcd
LSL r30               ;r30=000abcd0
OR r30,r8            ;r30=000abcde
LSL r30               ;r30=00abcde0
OR r30,r9            ;r30=00abcdef
LSL r30
LSL r30
out PortD,r30

mov r30,r10       ;r30=0000000g
out PortB,r30 


Start:
rjmp Start



