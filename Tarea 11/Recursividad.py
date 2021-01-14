class Stack:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def pop(self):
        if self.is_empty():
            print("Lista vacia")
        else:
            return self.__data.pop()

    def push(self, value):
        self.__data.append(value)

    def peek(self):
        return self.__data[len(self.__data) -1]

    def to_string(self):
        for item in self.__data: #Para invertir los valores: self.__data[::-1]
            print(f" | {item} | ")
            print(" -----")

print("Cuenta regresiva")
def countdown(num):
  num -= 1
  if num > 0:
    print(num)
    countdown(num)
  else:
    print("Se acabó!!")

def main():
  countdown(10)

main()

print("------------------------------")

print("Pila")
def medio(pila, media, posicion):
  if posicion < media:
        x = pila.pop()
        medio(pila, media, posicion+1)
        if posicion != media-1:
            pila.push(x)

def main2():
  pila = Stack()
  pila.push(1)
  pila.push(2)
  pila.push(3)
  pila.to_string()
  medio(pila, round(pila.length()/2), 0)
  print("Eliminando el valor medio")
  pila.to_string()

main2()
