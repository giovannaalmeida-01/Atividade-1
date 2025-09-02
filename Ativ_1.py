import random
import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            stack.append(node)
        else:
            stack.append(Node(token))
    return stack[0]

def infix_to_postfix(expression):
    prec = {'+':1, '-':1, '*':2, '/':2}
    output = []
    stack = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in prec:
            while stack and stack[-1] != '(' and prec[token] <= prec[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return output

def visualize_tree(root, filename):
    dot = graphviz.Digraph()
    def add_nodes_edges(node):
        if node:
            dot.node(str(id(node)), node.value)
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes_edges(node.right)
    add_nodes_edges(root)
    dot.render(filename, format='png', cleanup=True)

def generate_random_expression():
    ops = ['+', '-', '*', '/']
    nums = [str(random.randint(1, 9)) for _ in range(4)]
    expr = f"( {nums[0]} {random.choice(ops)} {nums[1]} ) {random.choice(ops)} ( {nums[2]} {random.choice(ops)} {nums[3]} )"
    return expr

# Árvore com valores fixos
expr1 = "( ( 8 + 4 ) * 10 )"
postfix1 = infix_to_postfix(expr1)
tree1 = build_expression_tree(postfix1)
visualize_tree(tree1, 'tree_fixed')

# Árvore com valores randômicos
expr2 = generate_random_expression()
postfix2 = infix_to_postfix(expr2)
tree2 = build_expression_tree(postfix2)
visualize_tree(tree2, 'tree_random')

print("Árvores geradas: tree_fixed.png e tree_random.png")
