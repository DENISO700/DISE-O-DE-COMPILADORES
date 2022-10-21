class Nodo:
    def __init__ (self, value):
        self.value = value  
        self.rightChild = None  
        self.leftChild = None

    def get(self):
        return self.value
    def set(self, value):
        self.value = value


class Bst:
        def __init__ (self):
            self.root = None
            self.signoPrioridad = { '+':1, '-':1, '*':2, '/':2, '^':3}
        
        def setRoot(self, value):
            self.root = Nodo(value)

        def getRoot(self):
            return self.root

        def add(self, value):
            if self.root is None:
                self.setRoot(value)
            else:
                self.addNode(self.root, value)

        def addNode(self, currentNode, value):

            if value in self.signoPrioridad:
                print('el signo encontrado es '+ value)

                #revisamos la prioridad de los signos
                if currentNode.value not in self.signoPrioridad: #aca pregunta si la raiz actiual es un numero
                    
                    nodoBackup = currentNode.value
                    #ponemos ese signo como padre
                    self.setRoot(value)
                    #el nodo raiz se vueleve hijo izquierdo
                    currentNode.leftChild = Nodo(nodoBackup)

                    print('---el padre es ahora: '+self.getRoot().value)
                    print('---el hijo izquierdo es: '+ currentNode.leftChild.value  + '\n')

                elif value in self.signoPrioridad and (self.signoPrioridad[value] >  self.signoPrioridad[currentNode.value]):
                    print("comparando "+value+ " con la raiz: "+currentNode.value)

                    nodeBackupDerecho = currentNode.rightChild.value

                    #Ponemos como nuevo hijo derecho al signo de mayor prioridad
                    currentNode.rightChild = Nodo(value)
                    print('el hijo derecho de '+self.getRoot().value+' es: '+ currentNode.rightChild.value)
                
                    #le ponemos como hijo izquierdo al backup previamente hecho
                    #currentNode.leftChild = Nodo(currentNode.rightChild.value)
                    #print('el hijo izquierdo de '+currentNode.rightChild.value+' es: '+ currentNode.leftChild)

                elif value in self.signoPrioridad and (self.signoPrioridad[value] <=  self.signoPrioridad[currentNode.value]):
                    print("comparando "+value+ " con la raiz: "+currentNode.value)
                    nodoBackup = currentNode.value
                    #ponemos ese signo como padre
                    self.setRoot(value)
                    #el nodo raiz se vueleve hijo izquierdo
                    currentNode.leftChild = Nodo(nodoBackup)

                    print('---el padre es ahora: '+self.getRoot().value)
                    print('---el hijo izquierdo es: '+ currentNode.leftChild.value  + '\n')
            
            else:
                
                if currentNode.rightChild:
                    self.addNode(currentNode.rightChild, value)
                else:
                    currentNode.rightChild = Nodo(value)
                    print('el hijo derecho de '+self.getRoot().value+' es: '+ currentNode.rightChild.value)


            # if currentNode.value >= value:
            #     if currentNode.leftChild:
            #         self.addNode(currentNode.leftChild, value)
            #     else:
            #         currentNode.leftChild = Nodo(value)
            # elif value > currentNode.value:
            #     if currentNode.rightChild:
            #         self.addNode(currentNode.rightChild, value)
            #     else:
            #         currentNode.rightChild = Nodo(value)
        def printTree(self):
            if self.root is not None:
                self._printTree(self.root)

        def _printTree(self, node):
            if node is not None:
                self._printTree(node.leftChild)
                print(str(node.value) + ' ')
                self._printTree(node.rightChild)

        def postorden(self):
            print("Imprimiendo árbol postorden: ")
            self._postorden_recursivo(self.root)
            print("")
        
        def _postorden_recursivo(self, raiz):
            if raiz is None:
                return None
            else:
                self._postorden_recursivo(raiz.leftChild)
                print(raiz.value, end=", ")
                self._postorden_recursivo(raiz.rightChild)
       
        

#3 + 2 * 9-16 / 4
arbol = Bst()

expresion = "3 + 2 * 9 - 16 / 4"
#expresion= "3 2 9 * + 16 4 / -"
expresion = expresion.split(" ")

print(expresion)

signoPrioridad = { '+':1, '-':1, '*':2, '/':2, '^':3}

salida = []


#vamos a hacerlo postfijo
for i in expresion:
    print('iteracion de '+ i)
    arbol.add(i)

arbol.postorden()



