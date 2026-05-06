class FunctionInfo():
    def __init__(self, arg1, arg2):
        self.__function_name = arg1
        self.__arg_count = arg2

    def returnFunctionName(self):
        return self.__function_name
    def returnArgCount(self):
        return self.__arg_count
