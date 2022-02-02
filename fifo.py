class ListFIFO():
    def __init__(self):
        self.__list = []
    def push(self,value):
        self.__list.append(value)
    def pop(self):
        return self.__list.pop(0)
    def print(self):
        print(self.__list)


from collections import deque
class dequeFIFO():
    def __init__(self):
        self.__q = deque()
    def push(self, value):
        self.__q.append(value)
    def pop(self):
        return self.__q.popleft()
    def print(self):
        print(self.__q)
