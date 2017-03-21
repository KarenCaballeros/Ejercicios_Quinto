notas= open("triangle.txt", "r")
lista_mayor = []
for linea in notas:	
	lista_mayor.append(linea.split(" "))
resultado = 0
elemento2= 0
for i in range(0, len(lista_mayor)):
	for elemento in lista_mayor[i]:
		elemento2 += 1
		if int(lista_mayor[i][elemento]) > int(lista_mayor[i][elemento2]:
			resultado += int(lista_mayor[i][elemento])
		else:
			resultado += int(lista_mayor[i][elemento2])
print(resultado)				
notas.close()