class CallerStack():
    def __init__(self):
        self.__functionsList = []

    def addFunction(self, functionInfo):
        self.__functionsList.append(functionInfo)
    def removeLastFunction(self):
        return self.__functionsList.pop()


    def returnLast(self):
        return self.__functionsList[-1]