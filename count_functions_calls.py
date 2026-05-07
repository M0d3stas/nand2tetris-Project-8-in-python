class CountFunctionCalls:
    def __init__(self):
        self.__functionList = []

    def addFunctionName(self, functionName):
        self.__functionList.append(functionName)

    def removeLastFunction(self):
        if len(self.__functionList) > 0:

            return self.__functionList.pop()

    def returnCountName(self, functionName):
        count = self.__functionList.count(functionName)
        return count

