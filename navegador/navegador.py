import requests

class Navegador(object):
	def __init__ (self, nombre):
		self.nombre=  nombre
		self.tabs= []

	def agregar_tab(self, tab):	
		self.tabs.append(tab)

	def eliminar_tab(self, cerrar):
		num = cerrar - 1
		self.tabs.pop(num)
	
	def contar_tabs(self):
		contador = 0
		for tab in self.tabs:
			contador += 1
		return contador		

	def cambiar_nombre(self, cambio, nuevo):
		num = cambio - 1
		self.tabs[num].url = nuevo


	def mostrar_tabs(self):
		num = 1
		resultado = ""
		for i in self.tabs:
			resultado+= str(num) + ". " + i.nombre + ", " + i.url + "\n"
			num += 1
		return resultado	
	
	def limpiar_tabs(self, eliminar):
		if eliminar == "si":
			self.tabs = []

	def guardar(self):
		doc = open("Tabs.txt", "w")
		doc.write(self.mostrar_tabs())
		doc.close()	

	def descargar(self, descargar):
		nume = descargar - 1
		r= requests.get(self.tabs[nume].url)
		docu = open("Descargas.txt", "w")
		docu.write(r.text)
		docu.close()