class Nodo:
    def __init__(self, valor=None):
        self.value = valor
        #self.padre = None       
        self.derecho=None
        self.izquierdo=None

class ArbolExpresiones():

    def __init__(self):
        self.raiz = None

    def setRoot(self,value):
        self.raiz = Nodo(value)



    def insertar(self,value):
        if self.raiz is None:
            self.setRoot(value)
        else:
            self._insertar(self.raiz, value)


    def _insertar(self, nodo, value):

        if value <= nodo.value:
            # Nos movemos a la izq si existe el hijo izq
            if nodo.izquierdo:
                self._insertar(nodo.izquierdo, value)
            else:
                nodo.izquierdo = Nodo(value)
                #nodo.izquierdo.padre = nodo
        elif value >= nodo.value:
            # Nos movemos a la der si existe el hijo der
            if nodo.derecho:
                self._insertar(nodo.derecho, value)
            else:
                nodo.derecho = Nodo(value)
                #nodo.derecho.padre = nodo

    def en_orden(self):
        self._en_orden(self.raiz)

    def _en_orden(self, nodo):
        if nodo is None:
            return None
        else:
            self._en_orden(nodo.izquierdo)
            print(nodo.value, end=' ')
            self._en_orden(nodo.derecho)


def get_key(val):

    operadores={
    
            '+':'1',
            '-':'1',
            '*':'2',
           '/':'2',


            }

    for key, value in operadores.items():
         if val == value:
             return key
 
    return "There is no such Key"


arbol = ArbolExpresiones()

expresion="20 + 5 * 4 + 6"

expresion=expresion.split(" ")

"""for x in expresion:
    arbol.insertar(x)"""



nodoIzq=""
padres=""
nodoDer=""
contadorApertur=0
contadorCierre=0

for i in range(len(expresion)):


    if get_key(expresion[i]):
        arbol.insertar(expresion[i])       
    else:
        arbol.insertar(expresion[i])

print(nodoIzq)
print(padres)
print(nodoDer)

arbol.en_orden()








        
