class Command():
    def __init__(self, commandRcv='',arg1='',arg2=0):
        self.__instrunction = commandRcv
        self.__argument1 = arg1
        self.__argument2 = arg2
        self.__validInstruction = False

    def setCommand(self,commandRCV):
        self.__instrunction = commandRCV
    
    def getCommand(self):
        return self.__instrunction

    def setArg1(self,arg1):
        self.__argument1 = arg1
    
    def getArg1(self):
        return self.__argument1

    def setArg2(self,arg2):
        self.__argument2 = arg2
    
    def getArg2(self):
        return self.__argument2
    
    def setValid(self, valid):
        self.__validInstruction = valid

    def getValid(self):
        return self.__validInstruction