class Conversion:
     
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False
             
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
         
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
             
            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)
 
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        #print ("".join(self.output))
 

def conversor(expresion):
    abecedario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    listaValores=[]
    #exp = "a+b*c-d/e"
    exp2 =expresion

    separado=exp2.split(" ") 
    indice=0 
    expFinal=""
    expFinal2=""
    for i in range(len(separado)):
        if separado[i].isnumeric():
            listaValores.append([abecedario[indice],separado[i]])
            indice=indice+1

  

    for i in range(len(separado)):
        for j in range(len(listaValores)):
            if separado[i]==listaValores[j][1]:
                separado[i]=listaValores[j][0]

 

    for i in separado:
        expFinal+=i

   


    #print(listaValores)
    #print(separado)
    #print(expFinal)

    obj = Conversion(len(expFinal))
    obj.infixToPostfix(expFinal)

    for i in range(len(obj.output)):
        for j in range(len(listaValores)):
            if obj.output[i]==listaValores[j][0]:
                obj.output[i]=listaValores[j][1]
    

    for i in obj.output:
        expFinal2+=i
        expFinal2+=" "



    #print("Expresion Infija Inicial: "+ str(exp2))
    #print("Expresion PostFija Final: "+ str(expFinal2))

    filtro=""
    for i in range(len(expFinal2)-1):
        filtro=filtro+expFinal2[i]




    return filtro

#exp2 = "3 + 2 * 9 - 16 / 4"
#print(conversor(exp2))



