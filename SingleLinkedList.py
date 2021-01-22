class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
    def updatedata(self,data):
        self.data=data
    def setlink(self,link):
        self.link=link
    def getdata(self):
        return self.data
    def getlink(self):
        return self.link

class LinkedList:
    def __init__(self):
        self.head=None

    def addToStart(self,data):
        tempNode=Node(data)
        tempNode.setlink(self.head)
        self.head=tempNode
        del tempNode

    def addToEnd(self,data):
        start=self.head
        tempNode=Node(data)
        while start.getlink():
            start=start.getlink()
        start.setlink(tempNode)
        del tempNode

    def length(self):
        start=self.head
        size=0
        while start:
            size+=1
            start=start.getlink()
        return size

    def index(self,data):
        start=self.head
        position=1
        while start:
            if start.getdata() == data:
                return position
            else:
                position+=1
                start=start.getlink()

    def Max(self):
        start=self.head
        largest = start.getdata()
        while start:
            if largest < start.getdata():
                largest=start.getdata()
            start=start.getlink()
        return largest

    def Min(self):
        start=self.head
        smallest=start.getdata()
        while start:
            if smallest > start.getdata():
                smallest=start.getdata()
            start=start.getlink()
        return smallest

    def atIndex(self,position):
        start=self.head
        position=int(position)
        pos=1
        while pos !=position :
            pos+=1
            start=start.getlink()

        data=start.getdata()
        return data

    def pop(self):
        start=self.head
        prv=None
        while start.getlink():
            prv=start
            start=start.getlink()

        if prv is None:
            self.head=None
        else:
            prv.setlink(None)
            # data = start.getdata()
            del start
            # return data

    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False
        while start:
            print(str(start.getdata()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

myList=LinkedList()

myList.addToStart(10)
myList.addToStart(12)
myList.addToStart(14)
myList.addToEnd(16)
myList.addToEnd(18)

print('Length = ',myList.length())

myList.display()

print('Index = ',myList.index(16))
print('Max Number = ',myList.Max())
print('Min Number = ',myList.Min())

myList.display()
myList.pop()
myList.display()
myList.pop()
myList.display()
