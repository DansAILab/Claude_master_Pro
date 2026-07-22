class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def contains(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)

root = None
for number in [5, 3, 8, 1, 4]:
    root = insert(root, number)

print(contains(root, 35))
print(contains(root, 8))