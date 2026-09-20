class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = BinaryNode(
    10,
    BinaryNode(
        5,
        BinaryNode(2),
        BinaryNode(7)
    ),
    BinaryNode(15)
)


# Завдання 1

def iterative_preorder(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

print("Iterative pre-order traversal:", iterative_preorder(root))

# Завдання 2

def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

print("Сума значень у BST:", sum_tree(root))