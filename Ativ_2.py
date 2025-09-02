import random
import graphviz

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)


    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)


    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
        
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp = self._min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursive(current_node.right, temp.value)
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1 
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)


    def depth(self, value):
        return self._depth_recursive(self.root, value, 0)

    def _depth_recursive(self, current_node, value, current_depth):
        if current_node is None:
            return -1 
        if current_node.value == value:
            return current_depth
        elif value < current_node.value:
            return self._depth_recursive(current_node.left, value, current_depth + 1)
        else:
            return self._depth_recursive(current_node.right, value, current_depth + 1)

    def visualize(self, filename="bst", format="png"):
        dot = graphviz.Digraph(comment='Binary Search Tree')
        dot.node(name='None', label='None', shape='plaintext')
        if self.root:
            self._visualize_recursive(self.root, dot)
        else:
            dot.node(str(None), 'Empty Tree')
        dot.render(filename, format=format, view=False)

    def _visualize_recursive(self, node, dot):
        if node is not None:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._visualize_recursive(node.left, dot)
            else:
                dot.node(str(node.value) + 'null_left', 'None', shape='plaintext')
                dot.edge(str(node.value), str(node.value) + 'null_left')

            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._visualize_recursive(node.right, dot)
            else:
                dot.node(str(node.value) + 'null_right', 'None', shape='plaintext')
                dot.edge(str(node.value), str(node.value) + 'null_right')
import graphviz
import random

if __name__ == "__main__":
    
    bst_fixed = BinarySearchTree()
    fixed_values = [146, 131, 124, 50, 150, 154, 188, 130, 30, 114, 57, 162, 16, 18, 119]
    print(f"Inserindo valores: {fixed_values}")
    for val in fixed_values:
        bst_fixed.insert(val)
    bst_fixed.visualize("bst_fixed_initial")
    print("bst_fixed_initial.png")

  
    search_value = 45
    print(f"Buscando o valor {search_value}: {bst_fixed.search(search_value)}")
    search_value = 100
    print(f"Buscando o valor {search_value}: {bst_fixed.search(search_value)}")


    delete_value = 30
    print(f"Removendo o valor {delete_value}")
    bst_fixed.delete(delete_value)
    bst_fixed.visualize("bst_fixed_after_delete")
    print("bst_fixed_after_delete.png")

    new_insert_value = 60
    print(f"Inserindo novo valor: {new_insert_value}")
    bst_fixed.insert(new_insert_value)
    bst_fixed.visualize("bst_fixed_after_insert")
    print("bst_fixed_after_insert.png")

    print(f"Altura da árvore: {bst_fixed.height()}")
    node_to_check_depth = 45
    print(f"Profundidade do nó {node_to_check_depth}: {bst_fixed.depth(node_to_check_depth)}")
    node_to_check_depth = 90
    print(f"Profundidade do nó {node_to_check_depth}: {bst_fixed.depth(node_to_check_depth)}")

    bst_random = BinarySearchTree()
    random_values = [random.randint(1, 200) for _ in range(15)]
    print(f"Inserindo valores aleatórios: {random_values}")
    for val in random_values:
        bst_random.insert(val)
    bst_random.visualize("bst_random_initial")
    print("bst_random_initial.png")
    print(f"Altura da árvore aleatória: {bst_random.height()}")