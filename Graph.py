class Graph:
    def __init__(self):
        self.numberofnodes=0
        self.adjacentlist={}

    def __str__(self):
        return str(self.__dict__)

    def addvertex(self,node):
        self.adjacentlist[node]=[]
        self.numberofnodes+=1

    def addedge(self,node1,node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)

    def showconnection(self):
        for x in self.adjacentlist:
            print(x , end=" --> ")
            for i in self.adjacentlist[x]:
                print(i , end=" ")

            print()


graph=Graph()

graph.addvertex('0')
graph.addvertex('1')
graph.addvertex('2')
graph.addvertex('3')
graph.addvertex('4')
graph.addvertex('5')
graph.addvertex('6')

graph.addedge('3','1')
graph.addedge('3','4')
graph.addedge('4','2')
graph.addedge('4','5')
graph.addedge('1','2')
graph.addedge('1','0')
graph.addedge('0','2')
graph.addedge('6','5')

print(graph)

print("\n")

graph.showconnection()