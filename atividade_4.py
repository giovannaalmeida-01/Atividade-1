import random
from graphviz import Digraph


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.counter = 0 

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} (H={root.height})", end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def visualize(self, node, name="avl_tree"):
        dot = Digraph()
        self._add_nodes_edges(node, dot)
        filename = f"{name}_{self.counter}"
        dot.render(filename, format="png", cleanup=True)
        print(f"Visualização salva como {filename}.png\n")
        self.counter += 1

    def _add_nodes_edges(self, node, dot):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes_edges(node.right, dot)


def demo_insertion_with_visualization(values, name_prefix):
    avl = AVLTree()
    for val in values:
        print(f"Inserindo {val}:")
        avl.root = avl.insert(avl.root, val)
        avl.visualize(avl.root, name=name_prefix)


def demo_random_insertion():
    values = random.sample(range(1, 100), 20)
    print("Inserindo valores aleatórios:", values)
    avl = AVLTree()
    for val in values:
        avl.root = avl.insert(avl.root, val)
    avl.visualize(avl.root, name="Valores_Aleatórios")


if __name__ == "__main__":
    demo_insertion_with_visualization([10, 20, 30], name_prefix="rotação_simples")

    demo_insertion_with_visualization([10, 30, 20], name_prefix="rotação_dupla")

    demo_random_insertion()

