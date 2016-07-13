from urllib2 import urlopen
from bs4 import BeautifulSoup

class Skyscraper():
	documento = None
	estado_del_clima = None

# Abrimos la pagina a scrapear y la transformamos en un documento de BS
	def leer_pagina(self):
		html = urlopen("http://www.tn.com.ar/clima")
		self.documento = BeautifulSoup(html.read(), 'html.parser')
		return self


# Buscamos la parte de la pagina que nos interesa
	def buscar_datos(self):
		self.estado_del_clima = self.documento.find(id="weather-header")		
		return self


# Eliminamos todo lo que no nos interesa
	def limpiar_los_datos_extraidos(self):
		self.estado_del_clima.form.extract()
		self.estado_del_clima.footer.extract()
		self.estado_del_clima.figure.extract()
		return self


# Lo escribimos en el template para poder usarlo
	def exportar_a_html_los_datos_extraidos(self):
		template_del_estado_del_clima = open("estado_del_clima.html", "w+")
		template_del_estado_del_clima.write(self.estado_del_clima.prettify('utf-8'))


# Podemos quedarnos solo con la informacion
	def exportar_a_texto_plano_los_datos_extraidos(self):
		informacion_del_estado_del_clima = open("estado_del_clima.txt", "w+")
		informacion_del_estado_del_clima.write(self.estado_del_clima.get_text().encode('utf-8'))


## Do the scraping

scraper = Skyscraper()
scraper.leer_pagina().buscar_datos().limpiar_los_datos_extraidos()

scraper.exportar_a_html_los_datos_extraidos()
scraper.exportar_a_texto_plano_los_datos_extraidos()
