class Node():
    def __init__(self, data=None):
        self.parent = None
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data):
        new_node = Node(data)
        new_node.parent = self
        if self.left == None:
            self.left = new_node
            return self
        else:
            raise Exception("Left is full")

    def add_right(self, data):
        new_node = Node(data)
        new_node.parent = self
        if self.right == None:
            self.right = new_node
            return self
        else:
            raise Exception("Right is full")

    def replace(self, data):
        self.data = data
        return self

    def num_child(self):
        if self.right != None and self.left != None:
            return 2
        elif self.right != None or self.left != None:
            return 1
        else:
            return 0

    def delete(self):
        current = self
        current_parent = self.parent
        current_left = self.left
        current_right = self.right

        if current_right != None and current_left != None:
            raise Exception("Node has 2 children")

        if current_right == None:
            if current_parent.left == current:
                self.left.parent = self.parent
                self.parent.left = self.left

            elif current_parent.right == current:
                self.left.parent = self.parent
                self.parent.right = self.left

            self.left = None
            self.parent = None

        elif current_right == None:
            if current_parent.left == current:
                self.right.parent = self.parent
                self.parent.left = self.right

            elif current_parent.right == current:
                self.right.paren = self.parent
                self.parent.right = self.right

            self.right = None
            self.parent = None

        return current

class Tree():
    def __init__(self):
        self.root = None

    def add_root(self,data):
        if self.root == None:
            self.root = Node(data)
            return self
        else:
            raise Exception ("Full")

def node_to_list(node = Node()):
    current = node
    if current == None:
        return None
    current_left = node.left
    current_right = node.right
    visit = [None, current]
    represent = [node.data]
    if current_left == None and current_right == None:
        return represent
    while current_left not in visit or current_right not in visit or current is not node:
        if current_left != None and current_left not in visit:
            represent.append(current_left.data)
            visit.append(current_left)
            current = current_left
        elif current_right != None and current_right not in visit:
            represent.append(current_right.data)
            visit.append(current_right)
            current = current_right
        else:
            current = current.parent
        current_left = current.left
        current_right = current.right

    return represent


def main():
    tree = Tree()
    tree.add_root(40)

    def tests():
        def test_add_root1():
            tree = Tree()
            expected = [10]
            result = node_to_list(tree.add_root(10))
            assert expected == result

        def test_add_left1():
            tree = Tree()
            tree.add_root(4)
            expected = [4,6]
            result = node_to_list(tree.root.add_left(7))
            assert expected == result

        def test_add_right1():
            tree = Tree()
            tree.add_root(6)
            expected = [6,8]
            result = node_to_list((tree.root.add_right(8)))
            assert expected == result

        def test_num_child1():
            tree = Tree()
            tree.add_root(2)
            expected = 0
            result = tree.root.num_child()
            assert expected == result

        def test_num_child2():
            tree = Tree()
            tree.add_root(2)
            tree.root.add_left(1)
            expected = 1
            result = tree.root.num_child()
            assert expected == result

        def test_num_child3():
            tree = Tree()
            tree.add_root(5)
            tree.root.add_right(10)
            tree.root.add_left(3)
            expected = 2
            result = tree.root.num_child()

        def test_replace1():
            tree = Tree()
            tree.add_root(4)
            expected = [9]
            result = node_to_list(tree.root.replace(9))
            assert expected == result

        def test_attach1():
            tree1 = Tree()
            tree2 = Tree()
            tree3 = Tree()
            tree1.add_root(3)
            tree2.add_root(6)
            tree2.root.add_left(5)
            tree2.root.add_right(7)
            tree3.add_root(9)
            tree3.root.add_left(8)
            tree3.root.add_right(10)
            expected = [3,6,5,7,9,8,10]
            result = node_to_list(tree1.root.attach(tree2,tree3))
            assert expected == result

        def test_delete1():
            tree = Tree()
            tree.add_root(12)
            tree.root.add_left(10)
            tree.root.left.add_left(14)
            expected = [10]
            result = node_to_list(tree.root.left.delete())
            assert expected == result

        test_add_root1()
        test_add_left1()
        test_add_right1()
        test_attach1()
        test_delete1()
        test_num_child1()
        test_num_child2()
        test_num_child3()
        test_replace1()
    tests()
main()