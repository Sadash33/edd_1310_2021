class NodoDoble:
    def __init__(self,value,siguiente,anterior):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 6

    def get_size(self):
        return self.__size

    def is_empty(self):
      return self.__head == None

    def append(self,value):
        if self.__size == 0:
            nuevo = NodoDoble(value,self.__tail,self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1

    def transversal(self):
        curr_node = self.__head.next
        while curr_node.next != None:
            print(curr_node.data,"->",end=" ")
            curr_node = curr_node.next
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail.prev
        while curr_node.prev != None:
            print(curr_node.data,"->",end=" ")
            curr_node = curr_node.prev
        print("")

    def find_from_head(self,value):
      curr_node = self.__head
      encontrado = None
      while curr_node.data != value:
        curr_node = curr_node.next

      if curr_node.data == value:
        encontrado = curr_node

      return encontrado

    def find_from_tail(self,value):
      curr_node = self.__tail
      encontrado = None
      while curr_node.data != value:
        curr_node = curr_node.prev

      if curr_node.data == value:
        encontrado = curr_node

      return encontrado

    def remove_from_head(self,value):
      curr_node = self.find_from_head(value)
      curr_node.prev.next = curr_node.next
      curr_node.next.prev = curr_node.prev
      curr_node.next = None
      curr_node.prev = None


    def remove_from_tail(self, value):
      curr_node = self.find_from_tail(value)
      curr_node.prev.next = curr_node.next
      curr_node.next.prev = curr_node.prev
      curr_node.next = None
      curr_node.prev = None





l = DoubleLinkedList()
print(f"La lista esta vacia? {l.is_empty()}")
print(f"Tamaño:  {l.get_size()}")
l.append(2)
l.append(10)
l.append(36)
l.append(15)
l.append(74)
l.append(28)
l.transversal()
l.reverse_transversal()
l.remove_from_head(74)
l.remove_from_tail(2)
l.transversal()
l.find_from_head(36)
