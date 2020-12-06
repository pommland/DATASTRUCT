class Node:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right = None

class BST():
    def insert(self,root,val):
        if not root :
            return Node(val)
        if val >= root.val :
            root.right = self.insert(root.right,val)
        else :
            root.left = self.insert(root.left,val)
        return root
    
    def delete(self,root,val):
        if not root :
            return Node(val)
        if val > root.val :
            root.right = self.delete(root.right,val)
        elif val < root.val :
            root.left = self.delete(root.left,val)
        else :
            if not root.right :
                temp = root.right
                root.right = None
                return temp
            if not root.right :
                temp = root.right
                root.right = None
                return temp
            temp = minvalNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,temp.val)
        return root


def printTree90(root,level=0):
    if root :
        printTree90(root.right,level+1)
        print("     " * level,root.val)
        printTree90(root.left,level+1)

def minvalNode(root):
    if not root :
        return root
    while root.left :
        root = root.left
    return root


if __name__ == "__main__":
    inp = input('Enter input: ').split(',')
    tree = BST()
    root = None 
    for str in inp :
        print(str)
        c,i =str.split(" ")
        if c == 'i':
            root = tree.insert(root, int(i))
        else:
            root = tree.delete(root, int(i))
            # print("Fuck")

        printTree90(root)
        print('===============================')