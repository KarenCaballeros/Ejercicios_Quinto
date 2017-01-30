import sys
import random

lista = []

for i in sys.argv:
	lista.append(i)

lista_letras= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
doc = open("passwords.txt", "w")
doc.write("Tus opciones de contraseña son: " + "\n")
num = 0
while num < int(lista[2]) :
	longitud = int(lista[1])
	opcion = ""
	while longitud > 0:
		opcion += (random.choice(lista_letras))
		longitud = longitud - 1
	num = num + 1
	doc.write(str(num) + ". ")
	doc.write((opcion) + "\n")		
	
doc.close()

print("listo, revisa tu escritorio.")