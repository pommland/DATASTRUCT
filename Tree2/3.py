class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


class BST:
    def __init__(self):
        self.root = None
    
    def add(self,val):
        string = ""
        if not self.root :
            self.root = Node(val)
        else :
            buffer = self.root
            while buffer is not None:
                if val < buffer.val:
                    string += 'L'
                    if buffer.left is None:
                        buffer.left = Node(val)
                        break
                    else:
                        buffer = buffer.left
                else:
                    string += 'R'
                    if buffer.right is None:
                        buffer.right = Node(val)
                        break
                    else:
                        buffer = buffer.right
        return string + '*'
    
    def print_tree90(self, node, level=0):
        if node is not None:
            self.print_tree90(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree90(node.left, level + 1)

exp = []


def inorder(node):
    global exp
    if node is not None:
        inorder(node.left)
        exp.append(int(node.val))
        inorder(node.right)


def ranking(lst, to_find):
    rank = 0
    for i in range(len(lst)):
        if to_find >= lst[i]:
            rank += 1
    return rank

if __name__ == "__main__":
    list_in  = input('Enter Input : ').split('/')
    data_list = [int(x) for x in list_in[0].split(" ")]
    find_rank = int( list_in[1])
    tree = BST()
    for item in data_list:
        tree.add(item)
    tree.print_tree90(tree.root)
    print('--------------------------------------------------')
    inorder(tree.root)
   
    print(f'Rank of {find_rank} : {ranking(exp, find_rank)}')

inorder(tree.root)