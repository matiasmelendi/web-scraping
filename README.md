# You can hear me but you can’t see me. Web scraping by robots: the silent invasion  

## Installing dependencies  

`pip install -r requirements.txt`
`npm install`

## Installing pip
If you don't have pip installed, follow the instructions on this link: https://pip.pypa.io/en/stable/installing/#id8

## Running the examples

### Defense against scraping bots blacklisting ips

`nodejs server.js`
`python charizardscraper.py`

### Defense against scraping using robots.txt

Just display the content of the robots.txt

### Malicious scraping: DoS attack

Scrapers are faster than humans reading a web page content, if we run a lot of scrapers at the same time we can cause a DoS attack.
* Change the number of scrapers created in `charizardscraper.py` to 10000.
* Then run `python charizardscraper.py`

### Inofensive scraping

`python skyscraper.py` 

### Scraping sites using javascript

`python selenium_robot.py`
