from urllib2 import urlopen
from bs4 import BeautifulSoup

# Abrimos la pagina a scrapear y la transformamos en un documento de BS
html = urlopen("http://www.tn.com.ar/clima")
documento = BeautifulSoup(html.read())

# Buscamos la parte de la pagina que nos interesa
estado_del_clima = documento.find(id="weather-header")

# Eliminamos todo lo que no nos interesa
estado_del_clima.form.extract()
estado_del_clima.footer.extract()
estado_del_clima.figure.extract()

# Lo escribimos en el template para poder usarlo
template_del_estado_del_clima = open("estado_del_clima.html", "w+")
template_del_estado_del_clima.write(estado_del_clima.prettify('utf-8'))

# Podemos quedarnos solo con la informacion
informacion_del_estado_del_clima = open("estado_del_clima.txt", "w+")
informacion_del_estado_del_clima.write(estado_del_clima.get_text().encode('utf-8'))