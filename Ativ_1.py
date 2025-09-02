import graphviz
import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.id = f"{value}_{random.randint(1, 10000)}"
        self.value = value
        self.left = left
        self.right = right

def generate_random_expression():
    operators = ['+', '-', '*', '/']

    operands = [str(random.randint(1, 9)) for _ in range(3)]

    ops = random.choices(operators, k=2)

    left_node = Node(ops[0], Node(operands[0]), Node(operands[1]))
    root = Node(ops[1], left_node, Node(operands[2]))

    expr_str = f"( ( {operands[0]} {ops[0]} {operands[1]} ) {ops[1]} {operands[2]} )"

    return root, expr_str

def visualize_tree(root, filename="arvore_aleatoria_1"):
    dot = graphviz.Digraph()

    def add_nodes_edges(node):
        if node is None:
            return
        dot.node(node.id, node.value)
        if node.left:
            dot.edge(node.id, node.left.id)
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(node.id, node.right.id)
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render(filename, format="png", view=True)

if __name__ == "__main__":
    root, expr = generate_random_expression()
    print("Expressão gerada aleatoriamente:", expr)
    visualize_tree(root, "arvore_aleatoria_1")
