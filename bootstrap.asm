@256
D=A
@SP
M=D
//Call Sys.init\n
//SAVE TO STACK
//Push working reg to stack
//push return address
@bootstrap$return
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL\n'
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//New ARG address
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(bootstrap$return)
