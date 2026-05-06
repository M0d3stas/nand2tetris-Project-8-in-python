from caller_stack import CallerStack
from function_call_info import FunctionCallInfo

#for call 
from count_functions_calls import CountFunctionCalls

class Translator():

    def __init__(self, filename, commandsList):
        self.__filename = filename
        self.__cmdList = commandsList
        

        #for fucntions translation
        self.__callerStack = CallerStack()
        self.__callFInfo = CountFunctionCalls()
        self.__currentFunctionName = 'None'

    def translateCommands(self):
        fullAsmCmd = ''
        jmp_label_counter = 0
        for command in self.__cmdList:
            cmd1 = command.getCommand()
            arg1 = command.getArg1()
            arg2 = command.getArg2()

            if cmd1 == 'push':
                if arg1 == 'constant':
                    fullAsmCmd += f'//push constant {arg2}\n'
                    fullAsmCmd +=f'@{arg2}\n'
                    fullAsmCmd += f'D=A\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n'
                    fullAsmCmd += f'M=D\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n'

                elif arg1 == 'static':
                    
                    fullAsmCmd += f'//push satic {arg2}\n'
                    fullAsmCmd +=f'@{self.__filename}.{arg2}\n' 
                    fullAsmCmd += f'D=M\n' #D=static.{arg2}[M]
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n' #A = SP[M]
                    fullAsmCmd += f'M=D\n' # *SP[A] = D
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n' #*SP + 1 
                elif arg1 == 'local':
                    
                    fullAsmCmd += f'//push local {arg2}\n'
                    fullAsmCmd +=f'@LCL\n' 
                    fullAsmCmd += f'D=M\n' #D=LCL[M]
                    fullAsmCmd += f'@{arg2}\n'
                    fullAsmCmd += f'A=D+A\n' 
                    fullAsmCmd += f'D=M\n' # D = *LCL[M]
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n' #A = SP[M]
                    fullAsmCmd += f'M=D\n' # *SP[A] = D
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n' #*SP + 1 

                elif arg1 == 'that':
                    fullAsmCmd += f'//push that {arg2}\n'
                    fullAsmCmd +=f'@THAT\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@{arg2}\n'
                    fullAsmCmd += f'A=D+A\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n'
                    fullAsmCmd += f'M=D\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n'
                
                elif arg1 == 'pointer':
                    if arg2 == '1':
                        fullAsmCmd += f'//push that {arg2}\n'
                        fullAsmCmd += f'@THAT\n' # @4
                        fullAsmCmd += f'D=M\n' #A= M[4]
                        fullAsmCmd += f'@SP\n' #A = 0
                        fullAsmCmd += f'A=M\n'
                        fullAsmCmd += f'M=D\n'
                        fullAsmCmd += f'@SP\n'
                        fullAsmCmd += f'M=M+1\n' #SP++
                    elif arg2 == '0':
                        fullAsmCmd += f'//push this {arg2}\n'
                        fullAsmCmd += f'@THIS\n' # @3
                        fullAsmCmd += f'D=M\n' #A= M[3]
                        fullAsmCmd += f'@SP\n' #A = 0
                        fullAsmCmd += f'A=M\n'
                        fullAsmCmd += f'M=D\n'
                        fullAsmCmd += f'@SP\n'
                        fullAsmCmd += f'M=M+1\n' #SP++

                elif arg1 == 'this':
                    fullAsmCmd += f'//push this {arg2}\n'
                    fullAsmCmd +=f'@THIS\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@{arg2}\n'
                    fullAsmCmd += f'A=D+A\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n'
                    fullAsmCmd += f'M=D\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n'

                elif arg1 == 'argument':
                    fullAsmCmd += f'//push argument {arg2}\n'
                    fullAsmCmd +=f'@ARG\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@{arg2}\n'
                    fullAsmCmd += f'A=D+A\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n'
                    fullAsmCmd += f'M=D\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n'
                
                elif arg1 == 'temp':
                    fullAsmCmd += f'//push temp {arg2}\n'
                    fullAsmCmd +=f'@5\n'
                    fullAsmCmd += f'D=A\n'
                    fullAsmCmd += f'@{arg2}\n'
                    fullAsmCmd += f'A=D+A\n'
                    fullAsmCmd += f'D=M\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n'
                    fullAsmCmd += f'M=D\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n'

            elif cmd1 == 'pop':
                if arg1 == 'local':
                    fullAsmCmd += f'//pop local {arg2}\n'
                    fullAsmCmd +=f'@LCL\n' #A=1
                    fullAsmCmd +=f'D=M\n' #D=M[1]
                    fullAsmCmd +=f'@{arg2}\n' #A= arg2
                    fullAsmCmd +=f'D=D+A\n' #D+arg2
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'M=D\n' #M[12]=D
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'A=M\n' #A=M[12]
                    fullAsmCmd +=f'M=D\n' #*r12/*LCL = D
                
                elif arg1 == 'static':
                    fullAsmCmd += f'//pop static {arg2}\n'
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@{self.__filename}.{arg2}\n' #A=1
                    fullAsmCmd +=f'M=D\n' #D=M[1]


                elif arg1 == 'argument':
                    fullAsmCmd += f'//pop argument {arg2}\n'
                    fullAsmCmd +=f'@ARG\n' #A=2
                    fullAsmCmd +=f'D=M\n' #D=M[2]
                    fullAsmCmd +=f'@{arg2}\n' #A=arg2
                    fullAsmCmd +=f'D=D+A\n' #D+arg2
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'M=D\n' #M[12]=D
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'A=M\n' #A=M[12]
                    fullAsmCmd +=f'M=D\n' #*r12/*ARG = D

                elif arg1 == 'this':
                    fullAsmCmd += f'//pop this {arg2}\n'
                    fullAsmCmd +=f'@THIS\n' #A=3
                    fullAsmCmd +=f'D=M\n' #D=M[3]
                    fullAsmCmd +=f'@{arg2}\n' #A=arg2
                    fullAsmCmd +=f'D=D+A\n' #D+arg2
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'M=D\n' #M[12]=D
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'A=M\n' #A=M[12]
                    fullAsmCmd +=f'M=D\n' #*r12/*LCL = D

                elif arg1 == 'that':
                    fullAsmCmd += f'//pop that {arg2}\n'
                    fullAsmCmd +=f'@THAT\n' #A=4
                    fullAsmCmd +=f'D=M\n' #D=M[4]
                    fullAsmCmd +=f'@{arg2}\n' #A=arg2
                    fullAsmCmd +=f'D=D+A\n' #D+arg2
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'M=D\n' #M[12]=D
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'A=M\n' #A=M[12]
                    fullAsmCmd +=f'M=D\n' #*r12/*LCL = D
                
                elif arg1 == 'temp':
                    fullAsmCmd += f'//pop temp {arg2}\n'
                    fullAsmCmd +=f'@5\n' #A=5
                    fullAsmCmd +=f'D=A\n' #D=5
                    fullAsmCmd +=f'@{arg2}\n' #A=arg2
                    fullAsmCmd +=f'D=D+A\n' #D+arg2
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'M=D\n' #M[12]=D
                    fullAsmCmd +=f'@SP\n' #A=0
                    fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                    fullAsmCmd +=f'D=M\n' #D=*SP
                    fullAsmCmd +=f'@R12\n' #A=12
                    fullAsmCmd +=f'A=M\n' #A=M[12]
                    fullAsmCmd +=f'M=D\n' #*r12/*ARG = D

                elif arg1 == 'pointer':
                    if arg2 == '1':
                        fullAsmCmd += f'//pop that {arg2}\n'
                        fullAsmCmd += f'@SP\n' #A=0
                        fullAsmCmd += f'AM=M-1\n' # A=M=M[0] -1
                        fullAsmCmd += f'D=M\n' #A= SP, D = *SP 
                        fullAsmCmd += f'@THAT\n' # @4
                        fullAsmCmd += f'M=D\n' 
                        
                    elif arg2 == '0':
                        fullAsmCmd += f'//pop this {arg2}\n'
                        fullAsmCmd += f'@SP\n' #A=0
                        fullAsmCmd += f'AM=M-1\n' # A=M=M[0] -1
                        fullAsmCmd += f'D=M\n' #A= SP, D = *SP 
                        fullAsmCmd += f'@THIS\n' # @4
                        fullAsmCmd += f'M=D\n' 
                        

            elif cmd1 == 'add':
                fullAsmCmd += f'//add\n'
                fullAsmCmd += f'@SP\n' #A=0
                fullAsmCmd += f'AM=M-1\n' #A=M =M[0]-1 
                fullAsmCmd += f'D=M\n' #D= *sp
                fullAsmCmd += f'A=A-1\n' #A = sp-1
                fullAsmCmd += f'M=D+M\n' #*SP = D + *SP
            
            elif cmd1 == 'sub':
                fullAsmCmd += f'//sub\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'M=M-D\n'

            elif cmd1 == 'neg':
                fullAsmCmd += f'//negative\n'
                fullAsmCmd += f'@SP\n' #A=0
                fullAsmCmd += f'A=M-1\n' #A=M[0]-1 
                fullAsmCmd += f'M=-M\n' #*SP= -*sp

            elif cmd1 == 'eq':
                fullAsmCmd += f'//eq\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'  #
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'D=M-D\n'  #result = x - y
                fullAsmCmd += f'@JMP_EQ_{jmp_label_counter}\n'       #address for jumping
                fullAsmCmd += f'D;JEQ\n'
                #X!=Y
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=0\n' #*SP = 0 (FALSE)
                fullAsmCmd += f'@JMP_END_{jmp_label_counter}\n'
                fullAsmCmd += f'0;JMP\n'
                #X=Y
                fullAsmCmd += f'(JMP_EQ_{jmp_label_counter})\n' 
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=-1\n' #*SP = -1 (TRUE)
    
                fullAsmCmd += f'(JMP_END_{jmp_label_counter})\n'
                jmp_label_counter += 1
            elif cmd1 == 'gt':
                fullAsmCmd += f'//gt\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'  #
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'D=M-D\n'  #result = x - y
                fullAsmCmd += f'@JMP_GT_{jmp_label_counter}\n'       #address for jumping
                fullAsmCmd += f'D;JGT\n'
                #x-y < 0
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=0\n' #*SP = 0 (FALSE)
                fullAsmCmd += f'@JMP_END_{jmp_label_counter}\n'
                fullAsmCmd += f'0;JMP\n'
                #x-y > 0
                fullAsmCmd += f'(JMP_GT_{jmp_label_counter})\n' 
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=-1\n' #*SP = -1 (TRUE)
    
                fullAsmCmd += f'(JMP_END_{jmp_label_counter})\n'
                jmp_label_counter += 1

            elif cmd1 == 'lt':
                fullAsmCmd += f'//lt\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'  #
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'D=M-D\n'  #result = x - y
                fullAsmCmd += f'@JMP_LT_{jmp_label_counter}\n'       #address for jumping
                fullAsmCmd += f'D;JLT\n'
                #x-y > 0
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=0\n' #*SP = 0 (FALSE)
                fullAsmCmd += f'@JMP_END_{jmp_label_counter}\n'
                fullAsmCmd += f'0;JMP\n'
                #x-y < 0
                fullAsmCmd += f'(JMP_LT_{jmp_label_counter})\n' 
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=-1\n' #*SP = -1 (TRUE)
    
                fullAsmCmd += f'(JMP_END_{jmp_label_counter})\n'
                jmp_label_counter += 1

            elif cmd1 == 'and':
                fullAsmCmd += f'//and\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'  #
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'M=D&M\n'  #x = x & y
            elif cmd1 == 'or':
                fullAsmCmd += f'//or\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'  #
                fullAsmCmd += f'A=A-1\n'
                fullAsmCmd += f'M=D|M\n'  #x = x | y
            elif cmd1 == 'not':
                fullAsmCmd += f'//not\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M-1\n'
                fullAsmCmd += f'M=!M\n'  # x = !x

            elif cmd1 == 'label':
                fullAsmCmd += f'//label {arg1}\n'
                fullAsmCmd += f'({self.__currentFunctionName}.{arg1})\n'
            elif cmd1 == 'goto':
                fullAsmCmd += f'//goto {self.__currentFunctionName}.{arg1}\n'
                fullAsmCmd += f'@{self.__currentFunctionName}.{arg1}\n'
                fullAsmCmd += f'0;JMP\n'
            elif cmd1 == 'if-goto':
                fullAsmCmd += f'//if-goto {self.__filename}.{self.__currentFunctionName}.{arg1}\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'AM=M-1\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@{self.__currentFunctionName}.{arg1}\n'
                fullAsmCmd += f'D;JNE\n'


            #functions translation
            elif cmd1 == 'function':
                self.__currentFunctionName = arg1
                fullAsmCmd += f'//Function {arg1}.{arg2}\n'
                fullAsmCmd += f'({arg1})\n'
                for x in range(int(arg2)):
                    fullAsmCmd += f'@0\n'
                    fullAsmCmd += f'D=A\n'
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'A=M\n' #A = SP[M]
                    fullAsmCmd += f'M=D\n' # *SP[A] = D
                    fullAsmCmd += f'@SP\n'
                    fullAsmCmd += f'M=M+1\n' #*SP + 1 

                if arg1 == "Sys.init":
                    functionInfo = FunctionCallInfo(arg1,arg2,1)
                    self.__callFInfo.addFunctionName(arg1)
                    self.__callerStack.addFunction(functionInfo)
            elif cmd1 == "call":
                self.__callFInfo.addFunctionName(arg1)
                insadeFunctionName = self.__callerStack.returnLast().returnFunctionName()
                counter = self.__callFInfo.returnCountName(insadeFunctionName)
                functionInfo = FunctionCallInfo(arg1,arg2,counter)
                fullAsmCmd += f'//Call {self.__filename}.{arg1} {arg2}\n'

                #SAVE TO STACK
                fullAsmCmd += f'//Push working reg to stack\n'
                fullAsmCmd += f'//push return address\n'
                fullAsmCmd +=f'@{insadeFunctionName}$ret.{counter}\n'
                fullAsmCmd += f'D=A\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'M=M+1\n'

                fullAsmCmd += f'//push LCL\n'
                fullAsmCmd +=f'@LCL\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'M=M+1\n'

                fullAsmCmd += f'//push ARG\n'
                fullAsmCmd +=f'@ARG\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'M=M+1\n'

                fullAsmCmd += f'//push THIS\n'
                fullAsmCmd +=f'@THIS\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'M=M+1\n'

                fullAsmCmd += f'//push THAT\n'
                fullAsmCmd +=f'@THAT\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'A=M\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'M=M+1\n'

                fullAsmCmd += f'//New ARG address\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@5\n'
                fullAsmCmd += f'D=D-A\n'
                fullAsmCmd += f'@{arg2}\n'
                fullAsmCmd += f'D=D-A\n'
                fullAsmCmd += f'@ARG\n'
                fullAsmCmd += f'M=D\n'

                fullAsmCmd += f'//LCL = SP\n'
                fullAsmCmd += f'@SP\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@LCL\n'
                fullAsmCmd += f'M=D\n'

                fullAsmCmd += f'@{arg1}\n'
                fullAsmCmd += f'0;JMP\n'
                fullAsmCmd += f'({insadeFunctionName}$ret.{counter})\n'
            
                self.__callerStack.addFunction(functionInfo)
                print(functionInfo.returnFunctionName())
            elif cmd1 == 'return':

                fullAsmCmd += f'//Return\n'
                fullAsmCmd += f'@LCL\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@R14\n'
                fullAsmCmd += f'M=D\n'
                fullAsmCmd += f'@5\n'
                fullAsmCmd += f'A=D-A\n'
                fullAsmCmd += f'D=M\n'
                fullAsmCmd += f'@R13\n'
                fullAsmCmd += f'M=D\n'

                #*ARG = pop()
                fullAsmCmd +=f'@SP\n' #A=0
                fullAsmCmd +=f'AM=M-1\n'#A=M=M[0]-1
                fullAsmCmd +=f'D=M\n' #D=*SP
                fullAsmCmd +=f'@ARG\n' #arg=3
                fullAsmCmd +=f'A=M\n' #A=256
                fullAsmCmd +=f'M=D\n' #ARG = return value

                #SP = ARG + 1
                fullAsmCmd +=f'D=A+1\n' #D= 257
                fullAsmCmd +=f'@SP\n'   #SP=0
                fullAsmCmd +=f'M=D\n'   #M[0] = 270 => 257

                
                #THAT = *(R14 -1)
                fullAsmCmd +=f'@R14\n' #ef = 265
                fullAsmCmd +=f'D=M-1\n'     #D=M[265] - 1
                fullAsmCmd +=f'A=D\n'
                fullAsmCmd +=f'D=M\n'       #D= M[A]
                fullAsmCmd +=f'@THAT\n'     #A=4
                fullAsmCmd +=f'M=D\n'       #M[4] = D

                #THIS = *(R14 -2)
                fullAsmCmd +=f'@2\n'
                fullAsmCmd +=f'D=A\n'
                fullAsmCmd +=f'@R14\n' #ef = 265
                fullAsmCmd +=f'A=M-D\n'     #A=M[265]-D
                fullAsmCmd +=f'D=M\n'       #D= M[A]
                fullAsmCmd +=f'@THIS\n'     #A=3
                fullAsmCmd +=f'M=D\n'       #M[3] = D

                #ARG = *(R14 -3)
                fullAsmCmd +=f'@3\n'
                fullAsmCmd +=f'D=A\n'
                fullAsmCmd +=f'@R14\n' #ef = 262
                fullAsmCmd +=f'A=M-D\n'     #A=M[262] - 3
                fullAsmCmd +=f'D=M\n'       #D= M[262]
                fullAsmCmd +=f'@ARG\n'      #A=2
                fullAsmCmd +=f'M=D\n'       #M[2] = D

                #LCL = *(R14 -4)
                fullAsmCmd +=f'@4\n'
                fullAsmCmd +=f'D=A\n'
                fullAsmCmd +=f'@R14\n' #ef = 265
                fullAsmCmd +=f'A=M-D\n'     #A=M[265] - D
                fullAsmCmd +=f'D=M\n'       #D= M[A]
                fullAsmCmd +=f'@LCL\n'      #A=1
                fullAsmCmd +=f'M=D\n'       #M[1] = D

                #goto retAddr
                fullAsmCmd +=f'@R13\n' #A=120
                fullAsmCmd +=f'A=M\n'         #A=M[120]
                fullAsmCmd += f'0;JMP\n'      #jmp r13ess


        __translatedToAsm = fullAsmCmd

        return __translatedToAsm