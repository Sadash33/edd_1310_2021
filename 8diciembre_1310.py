from Array2D import Array2D
from Stack import Stack

class LaberintoADT:
    '''
0 pasillo, 1 pared, S salida y E entrada
pasillo es una tupla ((2, 1), (2, 2), (2, 3 ), (2, 4), (3, 2), (4, 2))
entrada en una tupla (5, 1)
salida (2, 5)
    '''
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto = Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1], '0')
        self.set_entrada(entrada[0], entrada[1])
        self.set_salida(salida[0], salida[1])
        self.__camino = Stack()
        self.__previa = None #Guardará la posición previa 


    def to_string(self): #Muestra el laberinto
        self.__laberinto.to_string()

#Establece la entrada 'E' en la matriz, verificar límites.

    def set_entrada(self, ren, col):
        # Terminar la validación de las coordenadas
        self.__laberinto.set_item(ren, col, 'E')

#Establece la salida 'S' en la matriz, verificar límites periféricos

    def set_salida(self, ren, col):
        #Terminar las validaciiones
        self.__laberinto.set_item(ren, col, 'S')

    def es_salida(self, ren, col):
        return self.__laberinto.get_item(ren, col) == 'S'

    def buscar_entrada(self): #Busca la posición de la entrada y la mete a la pila
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                tope = self.__camino.peek() #Tupla
                if self.__laberinto.get_item(tope[0, tope[1]]) == 'E':
                    self.__camino.push((renglon, columna))
                    encontrado = True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def imprimir_camino(self):
        self.__camino.to_string()

    def get_pos_actual(self):
        return self.__camino.peek()

    def resolver_laberinto(self): #Aplicar reglas 
        actual = self.__camino.peek() #(5, 2)
        #Buscar izquierda
        if actual[1]-1 != -1 \ 
        and self.__laberinto.get_item(actual[0], actual[1]-1) == '0' \ 
        and self.get_previa() != (actualactual[0], actual[1]-1) \ 
        and self.__laberinto.get_item(actual[0], actual[1]-1) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0], actual[1]-1))

        #Buscar arriba
        elif actual[1]-1 != -1 \ 
        and self.__laberinto.get_item(actual[0]-1, actual[1]) == '0' \ 
        and self.get_previa() != (actualactual[0]-1, actual[1]) \ 
        and self.__laberinto.get_item(actual[0]-1, actual[1]-1) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0]-1, actual[1]))

       #Buscar derecha
        elif 1==0:
            pass

        #Buscar abajo
        elif 1==0:
            pass

        else:
            self.__laberinto.set_item(actual[0] actual[1], 'X')
            self.__previa = actual
            self.__camino.pop()


from Backtracking import LaberintoADT
pasillos_inicial = (2, 1), (2, 2), (2, 3 ), (2, 4), (3, 2), (4, 2)
lab = LaberintoADT(6, 6, pasillos_inicial, (5, 2), (2, 5))
lab.buscar_entrada()
lab.to_string()
lab.imprimir_camino()

while not lab.es_salida(lab.get_pos_actual()[0], lab.get_pos_actual()[1]):
    print("probar")
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)
        
