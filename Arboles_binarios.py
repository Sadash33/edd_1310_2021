class Nodoarbol:
  def __init__(self, value, left = None, right = None):
    self.data = value
    self.left = left
    self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        #Regla 1
        if self.__root == None:
            self.__root = Nodoarbol(value, None, None)
        #Regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe")
        elif value < nodo.data:
            #Regla 1
            if nodo.left == None:
                nodo.left = Nodoarbol(value)
            #Regla 2
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = Nodoarbol(value)
            else:
                self.__insert__(Nodoarbol.right, value)

    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=",")
            self.__recorrido_in(nodo.right)

    def transversal(self, format = "inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Recorrido en Pre")
        elif format == "Postorden":
            print("Postorden")
        else:
            print("Error, no existe el formato")
