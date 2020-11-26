class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


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

if __name__ == "__main__":
    data_list = [int(x) for x in input("Enter Input : ").split(" ")]
    tree = BST()
    for item in data_list:
        print(tree.add(item))