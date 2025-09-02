import random
from graphviz import Digraph

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, valor):
        def _insert(root, valor):
            if not root:
                return Node(valor)
            if valor < root.valor:
                root.left = _insert(root.left, valor)
            elif valor > root.valor:
                root.right = _insert(root.right, valor)
            return root
        self.root = _insert(self.root, valor)

    def search(self, valor):
        def _search(root, valor):
            if not root:
                return False
            if root.valor == valor:
                return True
            elif valor < root.valor:
                return _search(root.left, valor)
            else:
                return _search(root.right, valor)
        return _search(self.root, valor)

    def delete(self, valor):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, valor):
            if not root:
                return root
            if valor < root.valor:
                root.left = _delete(root.left, valor)
            elif valor > root.valor:
                root.right = _delete(root.right, valor)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _min_value_node(root.right)
                root.valor = temp.valor
                root.right = _delete(root.right, temp.valor)
            return root

        self.root = _delete(self.root, valor)

    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def depth(self, valor):
        def _depth(node, valor, current_depth=0):
            if not node:
                return -1
            if valor == node.valor:
                return current_depth
            elif valor < node.valor:
                return _depth(node.left, valor, current_depth + 1)
            else:
                return _depth(node.right, valor, current_depth + 1)
        return _depth(self.root, valor)

    def print_tree(self):
        def _print_tree(node, level=0, prefix="Root: "):
            if node:
                print(" " * (level * 4) + prefix + str(node.valor))
                if node.left or node.right:
                    _print_tree(node.left, level + 1, "L--- ")
                    _print_tree(node.right, level + 1, "R--- ")
        _print_tree(self.root)

    def visualize(self, filename='arvore_aleatoria_2'):
        dot = Digraph()
        def _add_edges(node):
            if not node:
                return
            dot.node(str(node.valor))
            if node.left:
                dot.node(str(node.left.valor))
                dot.edge(str(node.valor), str(node.left.valor))
                _add_edges(node.left)
            if node.right:
                dot.node(str(node.right.valor))
                dot.edge(str(node.valor), str(node.right.valor))
                _add_edges(node.right)
        _add_edges(self.root)
        dot.render(filename, view=True, format='png')

if __name__ == "__main__":
    bst = BinarySearchTree()

    numeros = random.sample(range(1, 201), 15)
    print("Números gerados aleatoriamente:", numeros)

    for n in numeros:
        bst.insert(n)

    print("\nÁrvore binária de busca (impressa em texto):")
    bst.print_tree()

    print("\nGerando visualização gráfica da árvore...")
    bst.visualize("arvore_aleatoria_2")

    print("\nAltura da árvore:", bst.height())

    valor_profundidade = random.choice(numeros)
    print(f"Profundidade do nó com valor {valor_profundidade}: {bst.depth(valor_profundidade)}")

    valor_busca = random.randint(1, 200)
    print(f"\nBusca pelo valor {valor_busca}: {'Encontrado' if bst.search(valor_busca) else 'Não encontrado'}")
