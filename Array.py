class Array:
    def __init__(self):
        self.lenght=0
        self.data={}

    def __str__(self):
        return str(self.data)

    def getlength(self):
        return self.lenght

    def push(self,item):
        self.data[self.lenght]=item
        self.lenght +=1

    def getindex(self,index):
        return self.data[index]

    def pop(self):
        lastitem = self.data[self.lenght-1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        return lastitem

    def delete(self,index):
        deleteitem=self.data[index]
        for i in range(index,self.lenght-1):
            self.data[i]=self.data[i+1]
        del self.data[self.lenght-1]
        self.lenght-=1
        return deleteitem

arr=Array()

arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')

print("Before Delete: ",arr)

arr.delete(3)

print("After Delete: ",arr)

print("Length: ",arr.getlength())