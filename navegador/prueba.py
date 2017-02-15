import requests
from navegador import Navegador
from tabs import Tab

print("BIENVENIDO.")
nom_navegador = input(str("Que navegador deseas usar: "))
objeto_navegador = Navegador(nom_navegador)
menu = 1
while menu != 8:
	print("""	
		MENU
	1. Crear nuevo tab.
	2. Cambiar URL de tab.
	3. Cerrar tab.
	4. Cerrar todos los tabs.
	5. Mostrar mis tabs.
	6. Guardar mis tabs.
	7. Descargar Tab.
	8. Salir.

		""")
	menu= int(input("Que desea hacer: "))

	if menu == 1:
		url= input("ingrese URL: ")
		nombre = input("ingrese nombre para el tab: ")
		objeto_tab = Tab(nombre , url)
		objeto_navegador.agregar_tab(objeto_tab)
	elif menu == 2:
		print("TABS en: ", objeto_navegador.nombre)
		print(objeto_navegador.mostrar_tabs())
		cambio= int(input("Ingrese numero de tab a cambiar: "))
		nuevo= input("ingrese el nuevo URL: ")
		objeto_navegador.cambiar_nombre(cambio, nuevo)
	elif menu == 3:
		print("TABS en: ", objeto_navegador.nombre)
		print(objeto_navegador.mostrar_tabs())
		cerrar= int(input("ingrese numero del tab a cerrar: "))
		objeto_navegador.eliminar_tab(cerrar)
	elif menu == 4:
		eliminar= input("Si usted esta seguro ingrese *si*: ")
		objeto_navegador.limpiar_tabs(eliminar)	
	elif menu == 5:
		print("TABS en: ", objeto_navegador.nombre)
		print(objeto_navegador.mostrar_tabs())
	elif menu == 6:
		objeto_navegador.guardar()
	elif menu == 7:
		print(objeto_navegador.mostrar_tabs())
		descargar= int(input("ingrese numero de tab a descargar: "))
		(objeto_navegador.descargar(descargar))
		
		

print("Gracias por usar ", objeto_navegador.nombre , ", vuelva pronto.")