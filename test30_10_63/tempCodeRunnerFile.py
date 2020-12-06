
inp = input('Enter input: ').split(',')
tree = AVL()
root = None
for ch in inp:
    c, i = ch.split()
    print(ch)
    if c == 'i':
        root = tree.insert(root, int(i))
    else:
        root = tree.delete(root, int(i))
        # print("asd")
    printTree90(root)
    print('===============================')
print(tree.BFS(root))
tree.preOrder(root)
print("")
tree.inOrder(root)
print("")
tree.postOrder(root)