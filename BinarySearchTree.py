class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree():
    pre_order = 'PREORDER'
    in_order = 'INORDER'
    post_order = 'POSTORDER'
    def __init__(self,root=None):
        self.root=root

    def get_root(self):
        return self.root

    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self.utility_insert(self.root,key)

    def utility_insert(self,this_node,key):
        if this_node.data > key:
            if this_node.left is None:
                this_node.left=Node(key)
            else:
                self.utility_insert(this_node.left,key)
        else:
            if this_node.right is None :
                this_node.right=Node(key)
            else:
                self.utility_insert(this_node.right,key)

    def inorder(self,this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.data,' ',end=' ')
            self.inorder(this_node.right)

    def preorder(self,this_node):
        if this_node:
            print(this_node.data,' ',end=' ')
            self.preorder(this_node.left)
            self.preorder(this_node.right)

    def postorder(self,this_node):
        if this_node:
            self.postorder(this_node.left)
            self.postorder(this_node.right)
            print(this_node.data,' ',end=' ')

    def print(self,traversal_type):
        if traversal_type.upper() == self.in_order:
            print("\nInorder Type")
            self.inorder(self.root)
        elif traversal_type.upper() == self.post_order:
            print("\nPostorder Type")
            self.postorder(self.root)
        else:
            print("\nPreorder Type")
            self.preorder(self.root)

    def search(self,this_node,key):
        if this_node is None:
            print("Key ( ",key," ) not found")
        elif this_node.data == key:
            print("Key ( ", key, " ) Found")
        elif this_node.data < key:
            self.search(this_node.rigth,key)
        else:
            self.search(this_node.left,key)

    def find_inorder_succesor(self, this_node):
        ptr = this_node

        while ptr.left is not None:
            ptr = ptr.left
        return ptr

    def remove(self,this_node,key):
        if this_node is None:
            return this_node
        elif this_node.data > key:
            this_node.right=self.remove(this_node.right,key)
        elif this_node.data <key:
            this_node.left = self.remove(this_node.left, key)

        else:
            if this_node.left is None:
                temp=this_node.right
                this_node=None
                return  temp
            elif this_node.right is None:
                temp=this_node.left
                this_node=None
                return temp


            temp= self.find_inorder_succesor(this_node.right)
            this_node.right=self.remove(this_node,temp.data)
        return temp


if __name__=='__main__':
    print('Binary Search TREE')

    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    print("1- Inorder Traversal")
    print("2- PostOrder Traversal")
    print("3- Preorder Traversal")

    choine=int(input("Enter Your Choice"))
    if choine == 1:
        bst.print("inorder")
    if choine == 1:
        bst.print("postorder")
    else:
        bst.print("preorder")
