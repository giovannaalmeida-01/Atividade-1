import random
import graphviz

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if no is None:
            return Node(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_rec(no.esquerda, valor)
        else:
            no.direita = self._inserir_rec(no.direita, valor)
        return no

    def inorder(self):
        return self._inorder_rec(self.raiz)

    def _inorder_rec(self, no):
        if no is None:
            return []
        return self._inorder_rec(no.esquerda) + [no.valor] + self._inorder_rec(no.direita)

    def preorder(self):
        return self._preorder_rec(self.raiz)

    def _preorder_rec(self, no):
        if no is None:
            return []
        return [no.valor] + self._preorder_rec(no.esquerda) + self._preorder_rec(no.direita)

    def postorder(self):
        return self._postorder_rec(self.raiz)

    def _postorder_rec(self, no):
        if no is None:
            return []
        return self._postorder_rec(no.esquerda) + self._postorder_rec(no.direita) + [no.valor]

    def visualizar_texto(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        if no.direita:
            self.visualizar_texto(no.direita, nivel + 1)
        print("   " * nivel + f"-> {no.valor}")
        if no.esquerda:
            self.visualizar_texto(no.esquerda, nivel + 1)

    def visualizar_graphviz(self):
        dot = graphviz.Digraph()
        self._add_nos_ao_dot(self.raiz, dot)
        dot.render('arvore_binaria', format='png', cleanup=True)
        print("'arvore_binaria.png'.")

    def _add_nos_ao_dot(self, no, dot):
        if no is not None:
            dot.node(str(no.valor))
            if no.esquerda:
                dot.edge(str(no.valor), str(no.esquerda.valor))
                self._add_nos_ao_dot(no.esquerda, dot)
            if no.direita:
                dot.edge(str(no.valor), str(no.direita.valor))
                self._add_nos_ao_dot(no.direita, dot)


valores = [55, 30, 80, 20, 45, 70, 90]
arvore = ArvoreBinaria()
for v in valores:
    arvore.inserir(v)

print("Visualização da Árvore (Texto):")
arvore.visualizar_texto()

arvore.visualizar_graphviz()

print("\nTravessia Inorder (Esquerda-Raiz-Direita):")
print(arvore.inorder())

print("\nTravessia Preorder (Raiz-Esquerda-Direita):")
print(arvore.preorder())

print("\nTravessia Postorder (Esquerda-Direita-Raiz):")
print(arvore.postorder())
