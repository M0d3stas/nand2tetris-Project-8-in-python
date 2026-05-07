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
//Function Sys.init.0
(Sys.init)
//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
//Call Class1.set 2
//Push working reg to stack
//push return address
@Sys.init$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
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
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Sys.init$ret.1)
//pop temp 0
@SP
AM=M-1
D=M
@5
M=D
//push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
//Call Class2.set 2
//Push working reg to stack
//push return address
@Sys.init$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
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
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Sys.init$ret.2)
//pop temp 0
@SP
AM=M-1
D=M
@5
M=D
//Call Class1.get 0
//Push working reg to stack
//push return address
@Sys.init$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
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
@Class1.get
0;JMP
(Sys.init$ret.3)
//Call Class2.get 0
//Push working reg to stack
//push return address
@Sys.init$ret.4
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
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
@Class2.get
0;JMP
(Sys.init$ret.4)
//label END
(Sys.init.END)
//goto Sys.init.END
@Sys.init.END
0;JMP
//Function Class1.set.0
(Class1.set)
//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop static 0
@SP
AM=M-1
D=M
@Class1.0
M=D
//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop static 1
@SP
AM=M-1
D=M
@Class1.1
M=D
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//Return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R13
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R14
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
//Function Class1.get.0
(Class1.get)
//push satic 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push satic 1
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//Return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R13
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R14
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
//Function Class2.set.0
(Class2.set)
//push argument 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop static 0
@SP
AM=M-1
D=M
@Class2.0
M=D
//push argument 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop static 1
@SP
AM=M-1
D=M
@Class2.1
M=D
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//Return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R13
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R14
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
//Function Class2.get.0
(Class2.get)
//push satic 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push satic 1
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//Return
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R13
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=A+1
@SP
M=D
@R14
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
