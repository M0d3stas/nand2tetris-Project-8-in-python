class FunctionCallInfo():
    def __init__(self, arg1, arg2, counter):
        self.__function_name = arg1
        self.__arg_count = arg2
        self.__counter = counter

    def returnFunctionName(self):
        return self.__function_name
    
    def increaseCounter(self):
        self.__counter += 1
    def returnArgCount(self):
        return self.__arg_count
    
    def returnCounter(self):
        return self.__counter