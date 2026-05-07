class CallerStack():
    def __init__(self):
        self.__functionsList = []

    def addFunction(self, functionInfo):
        self.__functionsList.append(functionInfo)
    def removeLastFunction(self):
        if len(self.__functionsList) > 0:
            return self.__functionsList.pop()

    def incrementCounter(self):
        if len(self.__functionsList) > 0:
            self.__functionsList[-1].increaseCounter()
    def returnLast(self):
        return self.__functionsList[-1]