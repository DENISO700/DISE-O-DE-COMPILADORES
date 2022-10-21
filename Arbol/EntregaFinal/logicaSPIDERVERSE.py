
from conversor import *
#expresion= "3 2 9 * + 16 4 / -"
expresion="4 5 2 - * 1 7 * 3 - / 1 2 / +"
expresion = expresion.split(" ")
exp2="3 + 2 * 9 - 16 / 4"
operadores=['-','*','/','+']
posicion=0


def crearArbol(expresion):
	print(" ")
	print(expresion)
	print(" ")
	for i in reversed(range(len(expresion))):

		if expresion[i] in operadores:
			#caso S
			if expresion[i-1] in operadores:
				#caso NN
				if (expresion[i-2] not in operadores) and (expresion[i-3] not in operadores):


					if len(expresion)>3:
						print("Raiz:"+expresion[i])
						print("Hijo Derecho de :"+expresion[i] + " es " + expresion[i-1])
						print("Hijo Derecho de :"+expresion[i-1] + " es " + expresion[i-2])
						print("Hijo Izquierdo de :"+expresion[i-1] + " es " + expresion[i-3])
						expresion.pop(i-1)
						expresion.pop(i-2)
						expresion.pop(i-3)
						crearArbol(expresion)
					elif len(expresion)>2:

						print("Raiz:"+expresion[i])
						print("Hijo Derecho de :"+expresion[i] + " es " + expresion[i-1])
						print("Hijo Derecho de :"+expresion[i-1] + " es " + expresion[i-2])
						expresion.pop(i-1)
						expresion.pop(i-2)
						crearArbol(expresion)
					elif len(expresion)==1:
						print("Raiz:"+expresion[i])
						print("Hijo Derecho de :"+expresion[i] + " es " + expresion[i-1])
						expresion.pop(i-1)
						print("Finalizo")
				#caso SN
				elif (expresion[i-2] in operadores) and (expresion[i-3] not in operadores):
					print("Hijo Izquierdo de :"+expresion[i] + " es " + expresion[i-1])
					expresion.pop(i)
					crearArbol(expresion)

				#caso NS
				#https://www.infor.uva.es/~cvaca/asigs/AlgInfPost.htm --->caso faltante
				elif (expresion[i-2] not in operadores) and (expresion[i-3]  in operadores):
					print("Hijo Izquierdo de :"+expresion[i] + " es " + expresion[i-1])
					expresion.pop(i-1)
					expresion.pop(i-2)
					crearArbol(expresion)

			else:
				
				print("Hijo Izquierdo de :"+expresion[i] + " es " + expresion[i-1])
				expresion.pop(i)
				crearArbol(expresion)

		elif expresion[i-1] not in operadores :

			print("Hoja:"+expresion[i])
		break

#corregir hojas en medi odel arbol 
			

valor=conversor(exp2).split(" ")


crearArbol(valor)















		