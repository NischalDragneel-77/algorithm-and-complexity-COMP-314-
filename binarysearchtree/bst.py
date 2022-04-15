class node:
    def __init__(self,key,value):
        self.left=None
        self.right=None
        self.parent=None
        self.key=key
        self.value=value

class BinarySearchTree:
    def __init__(self):
        self.no_of_nodes=0
        self.root= None

    def add(self,key,value):
        newNode=node(key,value)
        if self.no_of_nodes==0:
            self.root=newNode
            self.no_of_nodes += 1
        else:
            temp=self.root
            while temp!=None:
                y=temp
                if newNode.key<temp.key:
                    temp=temp.left
                else:
                    temp=temp.right
            newNode.parent=y
            if newNode.key<y.key:
                y.left=newNode
            else:
                y.right=newNode
            self.no_of_nodes+=1

    def search(self,key):
        node=self.recursive_search(self.root,key)
        if node:
            return node.value
        else:
            return False

        
    def recursive_search(self,node: node,key):
        if node==None:
            return False
        if key<node.key:
            return self.recursive_search(node.left,key)
        elif key>node.key:
            return self.recursive_search(node.right,key)
        else:
            return node
            
    def smallest(self):
        smallestNode=self._smallest(self.root)
        return (smallestNode.key,smallestNode.value)
    
    def _smallest(self, node:node):
        if node!=None:
            temp=node
            while temp.left!=None:
                temp=temp.left
            return temp
        return

    def largest(self):
        largestNode=self._largest(self.root)
        return (largestNode.key,largestNode.value)

    def _largest(self,node:node):
        if node!=None:
            temp=node
            while temp.right!=None:
                temp=temp.right
            return temp
        return
        
    def preorder_walk(self):
        walk=[]
        self.preorder_traversal(self.root,walk)
        return walk
    
    def preorder_traversal(self,node:node,walk:list):
        if node!=None:
            walk.append(node.key)
            self.preorder_traversal(node.left,walk)
            self.preorder_traversal(node.right,walk)
        return

    def postorder_walk(self):
        walk=[]
        self.postorderr_traversal(self.root,walk)
        return walk

    def postorderr_traversal(self,node:node,walk:list):
        if node!=None:
            self.postorderr_traversal(node.left,walk)
            self.postorderr_traversal(node.right,walk)
            walk.append(node.key)
        return
    def inorder_walk(self):
        walk=[]
        self.inorderr_traversal(self.root,walk)
        return walk

    def inorderr_traversal(self,node:node,walk:list):
        if node!=None:
            self.inorderr_traversal(node.left,walk)
            walk.append(node.key)
            self.inorderr_traversal(node.right,walk)
        return

    def remove(self,key):
        if self.no_of_nodes==0:
            return False
        else:
            return self._remove(self.root,key)
            
    def _remove(self,root:node,key):
        nodeToDelete= self.recursive_search(root,key)
        if nodeToDelete is False:
            return False
        #case 1: no children
        if nodeToDelete.left is None and nodeToDelete.right is None:
            if nodeToDelete!=self.root:
                if nodeToDelete.parent.left==nodeToDelete:
                    nodeToDelete.parent.left=None
                    del nodeToDelete
                    self.no_of_nodes-=1
                else:
                    nodeToDelete.parent.right=None
                    del nodeToDelete
                    self.no_of_nodes-=1
            else:
                self.root=None
                del nodeToDelete
                self.no_of_nodes-=1
        #case 2: 2 children
        elif nodeToDelete.left and nodeToDelete.right:
            successorNode=self._largest(nodeToDelete.left)
            key=successorNode.key
            value=successorNode.value
            self._remove(self.root,successorNode.key)
            nodeToDelete.key=key
            nodeToDelete.value=value
        #case 3: only 1 child
        else:
            if nodeToDelete.left:
                child=nodeToDelete.left
            else:
                child=nodeToDelete.right
            if nodeToDelete!=self.root:
                if nodeToDelete==nodeToDelete.parent.left:
                    nodeToDelete.parent.left=child
                    del nodeToDelete
                    self.no_of_nodes-=1
                else:
                    nodeToDelete.parent.right=child
                    del nodeToDelete
                    self.no_of_nodes-=1
            else:
                self.root=child
                del nodeToDelete
                self.no_of_nodes-=1
        return

    def size(self):
        return self.no_of_nodes

if __name__=='__main__':
    bst=BinarySearchTree()
    bst.add(11, "Value for 11")
    bst.add(2, "Value for 2")
    bst.add(3, "Value for 3")
    bst.add(7, "Value for 7")
    bst.add(17, "Value for 17")
    bst.add(19, "Value for 19")
    bst.add(27, "Value for 27")
    bst.add(5, "Value for 5")
    print(bst.search(19))
    bst.remove(19)
    print(bst.search(19))
    print(bst.smallest())
    print(bst.largest())
    print(bst.preorder_walk())
    print(bst.postorder_walk())
    print(bst.inorder_walk())
    







    