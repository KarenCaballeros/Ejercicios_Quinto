print("1. Calcular area derectangulo")
print("2. Calcular area de triangulo")
print("3. Calcular area de circulo")
a=str(input("Ingrese la opcion que desee realizar"))

if a="1":
	b=float(input("Ingrese la base del rectangulo"))
	c=float(input("Ingrese la altura del rectangulo"))
	print("El area del rectangulo es ",b*a)
elif a="2":
	b=float(input("Ingrese la base del Triangulo"))
	c=float(input("Ingrese la altura del Triangulo"))
	print("El area del triangulo es ",((b*a)/2))
elif a="3":
	b=float(input("Ingrese el radio del circulo"))
	print("El area del circulo es ",3.1416*b)