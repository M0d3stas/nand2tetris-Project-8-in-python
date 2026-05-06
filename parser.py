import os

from command import Command

class Parser():
    
    def __init__(self,filename, lineOfInstrunction=''):
        self.__filename = filename
        self.__base_filename = ''
        self.__just_filename = ''
        self.__instLine = lineOfInstrunction
        self.__command = Command()

    def parseFilename(self):
            
        self.__base_filename = os.path.basename(self.__filename)  # → 'BasicTest.vm'       # → ('BasicTest', '.vm')
        self.__just_filename = os.path.splitext(self.__base_filename)[0] 
        return self.__just_filename

    def insertLine(self,line):
        self.__instLine = line

    def getCurrentLine(self):
        return self.__instLine

    def parseCommand(self):

        self.__command = Command()

        readCommand = True
        readArg1 = False
        readArg2 = False
        charCounter = 0
        validInst = False


        commandExtracted = ''
        arg1Extracted = ''
        arg2Extracted = ''


        for char in self.__instLine:
            if char == "/" or char == '\n' or char == '\\':
                break;

            if char == '\t':
                pass

            elif char == " ":
                if readCommand:
                    readCommand = False
                    readArg1 = True
                elif readArg1:
                    readArg1 = False
                    readArg2 = True
                elif readArg2:
                    readArg1 = False
                    readArg2 = True
                else:
                    break;
            elif readCommand:
                commandExtracted += char
                charCounter += 1
                validInst = True
            elif readArg1:
                arg1Extracted += char
                charCounter += 1
            elif readArg2:
                arg2Extracted += char
                charCounter += 1

        self.__command.setCommand(commandExtracted)
        self.__command.setArg1(arg1Extracted)
        self.__command.setArg2(arg2Extracted)
        self.__command.setValid(validInst)

        return self.__command
