//pop local 0. 2
@LCL //1
D=M //D=M[1](260)
@0 //A=0
D=D+A //260+0
@R12 //A=12
M=D //M[12] = 260

@SP //A=0
AM = M-1 // M[0](200) - 1 = AM(199) 
D=M //D= M[199] *SP(15)

@R12 //A=12
A=M //A=M[12] (260)
M=D // M[260] = 15


push local 0
push that 5
add

@SP  //A = 0
AM=M-1  // A = M[0]
D=M // D = *SP
@R12 // A=12
M = D // M[12] = D
@SP    // A = 0
AM=M-1  // A = M[0] - 1
D=M     // D= *SP 
@R12
D=D+M  // D= *SP + M[12]
@SP    // A=0
A=M    /// A=M[0] (*SP)
M=D    //*SP = D(addition result)
@SP
M=M+1  //increment SP

@SP
AM=M-1
D=M
A=A-1
M=D+M

#sub

@SP
AM=M-1
D=M
A=A-1
M=M-D









