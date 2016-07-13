from urllib2 import urlopen
from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import Chrome

class Scraper():
	documento = None
	html = None

	def leer_pagina_y_extraer_datos(self):
		with closing(Chrome()) as browser:
			browser.get("http://rocapp-test.herokuapp.com/usuarios/sign_in")
			username_field = browser.find_element_by_id("usuario_nombre_de_usuario")
			username_field.send_keys("Pepe")
			password_field = browser.find_element_by_id("usuario_password")
			password_field.send_keys("password")
			browser.find_element_by_name("commit").click()

			self.documento = BeautifulSoup(browser.page_source.encode('utf-8'), 'html.parser')

		return self

	def exportar_a_html_los_datos_extraidos(self):
		datos_extraidos = open("defensa_usando_javascript.html", "w+")
		datos_extraidos.write(self.documento.prettify())

## Do the scraping

scraper = Scraper()
scraper.leer_pagina_y_extraer_datos().exportar_a_html_los_datos_extraidos()