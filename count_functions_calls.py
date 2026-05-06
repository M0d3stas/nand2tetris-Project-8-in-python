class CountFunctionCalls:
    def __init__(self):
        self.__functionList = []

    def addFunctionName(self, functionName):
        self.__functionList.append(functionName)

    def returnCountName(self, functionName):
        count = self.__functionList.count(functionName)
        return count

