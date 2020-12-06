class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

class BST:
    def insert(self, root, val):
        if root == None :
            root = Node(val)
        else :
            cur = root
            state = False
            while not state:
                if cur.val >= val:
                    if cur.left == None:
                        cur.left = Node(val)
                        state = True
                    else :
                        cur = cur.left    
                else :
                    if cur.right == None:
                        cur.right = Node(val)
                        state = True
                    else :
                        cur = cur.right 
        return root

    def inserrrrrrrrrrrrrt(self, root, val):
        if not root:
            return Node(val)
        
        if val >= root.val:
            root.right = self.inserrrrrrrrrrrrrt(root.right, val)
        else:
            root.left = self.inserrrrrrrrrrrrrt(root.left, val)

        return root

    def deleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeete(self, root, val):
        if not root:
            return root

        if val > root.val:
            root.right = self.deleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeete(root.right, val)
        elif val < root.val:
            root.left = self.deleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeete(root.left, val)
        else:
            if not root.right:
                temp = root.left
                root.left = None
                return temp
            if not root.left:
                temp = root.right
                root.right = None
                return temp

            temp = miniValueeeeeeeeeeeeeeeeeNadode(root.right)
            root.val = temp.val
            root.right = self.deleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeete(root.right, temp.val)

        return root
            

def miniValueeeeeeeeeeeeeeeeeNadode(r):
    if not r:
        return r
    
    while r.left:
        r = r.left

    return r

def printTree90(root, level=0):
    if root:
        printTree90(root.right, level + 1)
        print('    ' * level, root.val)
        printTree90(root.left, level + 1)


if __name__ == "__main__":
    inp = input('Enter input: ').split(',')
    tree = BST()
    root = None
    for ch in inp:
        c, i = ch.split()
        print(ch)
        if c == 'i':
            root = tree.inserrrrrrrrrrrrrt(root, int(i))
        else:
            root = tree.deleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeete(root, int(i))
        printTree90(root)
        print('===============================')
