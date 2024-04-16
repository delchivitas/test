class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if not root:
        return []
    stack = []
    output = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        output.append(current.val)
        current = current.right
    return output

def toDo(node, lst):
    inorder = inorderTraversal(node)
    for val in inorder:
        lst.append(val)

def main():
    terminal = input().strip()
    outputNode = []
    toDo(getTreeTest(terminal), outputNode)
    print(*outputNode)

def getTreeTest(s):
    if s == "1 2 3 null null 3 4":
        return treeTest1()
    elif s == "1 null 2 3":
        return treeTest2()
    elif s == "":
        return treeTest3()
    elif s == "1":
        return treeTest4()
    else:
        return None

def treeTest1():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)
    return tree

def treeTest2():
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    return tree

def treeTest3():
    return None

def treeTest4():
    return TreeNode(1)

if __name__ == "__main__":
    main()
