class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_sample_tree():
    root = node(4)
    root.left = node(2)
    root.right = node(6)

    root.left.left = node(1)
    root.left.right = node(3)

    root.right.left = node(5)
    root.right.right = node(7)
    return root


def check(root, min, max):
    if root is None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)


def check_binary_tree_(root):
    return check(root, 0, 10000)


root_node = build_sample_tree()
result =check_binary_tree_(root_node)
print(result)
