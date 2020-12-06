class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def getHeight(self,root):
        if not root:
            return 0 
        else :
            return root.height

    def BFS(self,root):
        if not root:
            return
        else :
            q = []
            q.append(root)
            s =""
            while len(q) != 0 :
                n = q.pop(0)
                s += str(n.val) + " "
                if  n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
            return s
                

    def inOrder(self,root):
        if not root :
            return
        self.inOrder(root.left)
        print(root.val,end=" ")
        self.inOrder(root.right)

    def preOrder(self,root):
        if not root :
            return
        print(root.val,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self,root):
        if not root :
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val,end=" ")

    
    def getBalance(self,root):
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def rotateRight(self,z):
        y = z.left
        T3 = y.right

        z.left = T3
        y.right = z

        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def rotateLeft(self,z):
        y = z.right
        T2 =y.left

        z.right = T2
        y.left = z

        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def insert(self,root,val):
        if not root :
            return Node(val)
        
        if val >=  root.val :
            root.right =  self.insert(root.right,val)
        else : 
            root.left =  self.insert(root.left,val)
        
        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and root.left.val > val :
            return self.rotateRight(root)
        if balance < -1 and root.right.val < val :
            return self.rotateLeft(root)
        if balance > -1 and root.left.val < val :
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and root.right.val > val :
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        
        return root
    
    def delete(self,root,val):
        if not root :
            return root
        if val >  root.val :
            root.right =  self.delete(root.right,val)
        elif val <  root.val :
            root.left =  self.delete(root.left,val)
        else :
            if not root.right :
                temp = root.left
                root.left = None
                return temp
            if not root.left:
                temp = root.right
                root.right = None
                return temp
            temp = minValNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)
        
        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0 :
            return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) <= 0 :
            return self.rotateLeft(root)
        if balance > 1 and self.getBalance(root.left) < 0 :
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) > 0 :
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        
        return root

    
def minValNode(r):
    if not r:
        return r
    while r.left :
        r = r.left
    return r

def printTree90(root,level=0):
    if root :
        printTree90(root.right,level+1)
        print("    " * level , root.val)
        printTree90(root.left,level+1)



inp = input('Enter input: ').split(',')
tree = AVL()
root = None
for ch in inp:
    c, i = ch.split()                                  