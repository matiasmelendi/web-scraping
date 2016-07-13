from urllib2 import urlopen
from bs4 import BeautifulSoup
import threading
import itertools


class CharizardScraper():
	def scrapear(self):
		html = urlopen("http://localhost:3000/")
		documento = BeautifulSoup(html.read(), 'html.parser')

		print("Pedido terminado exitosamente!")

	def crear_scrapers(self, numero_de_scrapers):
		self.scrapers = []
		for _ in itertools.repeat(None, numero_de_scrapers):
			self.scrapers.append(threading.Thread(target=self.scrapear))
			
		return self	

	def iniciar_scraping(self):
			for scraper in self.scrapers: scraper.start()


CharizardScraper().crear_scrapers(10).iniciar_scraping()