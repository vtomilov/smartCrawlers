#!/usr/bin/python
from subprocess import Popen

start_urls = [
'http://beautydiscount.ru/catalog/everyday-minerals-ssha?page=all',
'http://beautydiscount.ru/catalog/lumene-finlyandiya?page=all',
'http://beautydiscount.ru/catalog/pupa?page=all',
'http://beautydiscount.ru/catalog/opi-ssha?page=all',
'http://beautydiscount.ru/catalog/londa-germaniya',
'http://beautydiscount.ru/catalog/weleda-germaniya?page=all',
'http://beautydiscount.ru/catalog/rimmel-velikobritaniya?page=all',
'http://beautydiscount.ru/catalog/revlon-professional-ispaniya?page=all',
'http://beautydiscount.ru/catalog/maybelline?page=all',
'http://beautydiscount.ru/catalog/max-factor-ssha?page=all',
 'http://beautydiscount.ru/catalog/anna-lotan-izrail?page=all',
 'http://beautydiscount.ru/catalog/anny-cosmetics-germaniya?page=all',
 'http://beautydiscount.ru/catalog/batiste-velikobritaniya-',
 'http://beautydiscount.ru/catalog/beauty-blender-ssha',
 'http://beautydiscount.ru/catalog/beauty-essential-rossiya',
 'http://beautydiscount.ru/catalog/biotherm-frantsiya?page=all',
 'http://beautydiscount.ru/catalog/crest_3d_white',
 'http://beautydiscount.ru/catalog/carmex-ssha',
 'http://beautydiscount.ru/catalog/embryolisse-frantsiya-?page=all',
 'http://beautydiscount.ru/catalog/dose-of-colors-ssha?page=all',
 'http://beautydiscount.ru/catalog/helena-rubinstein-avstraliya?page=all',
 'http://beautydiscount.ru/catalog/invisibobble-?page=all',
 'http://beautydiscount.ru/catalog/japan-gals-yaponiya?page=all',
 'http://beautydiscount.ru/catalog/mythic-oil---dlya-zaschity',
 'http://beautydiscount.ru/catalog/hairchalk---makiyazh-dlya-volos',
 'http://beautydiscount.ru/catalog/lime-crime-ssha?page=all',
 'http://beautydiscount.ru/catalog/lucas-papaw-remedies-avstraliya',
 'http://beautydiscount.ru/catalog/macadamia-natural-oil-ssha',
 'http://beautydiscount.ru/catalog/mizon-koreya?page=all',
 'http://beautydiscount.ru/catalog/moroccanoil-izrail?page=all',
 'http://beautydiscount.ru/catalog/missha-koreya?page=all',
 'http://beautydiscount.ru/catalog/nyx-ssha?page=all',
 'http://beautydiscount.ru/catalog/organic-shop-rossiya?page=all',
 'http://beautydiscount.ru/catalog/redken-ssha?page=all',
 'http://beautydiscount.ru/catalog/sally-hansen-ssha?page=all',
 'http://beautydiscount.ru/catalog/sleek_makeup?page=all',
 'http://beautydiscount.ru/catalog/tangle-teezer-velikobritaniya?page=all',
 'http://beautydiscount.ru/catalog/thebalm-ssha-?page=all',
 'http://beautydiscount.ru/catalog/tony-moly-koreya?page=all',
 'http://beautydiscount.ru/catalog/yves-saint-laurent-frantsiya?page=all',
 'http://beautydiscount.ru/catalog/wet-and-wild-ssha?page=all',
 'http://beautydiscount.ru/catalog/real-techniques-ssha',
 'http://beautydiscount.ru/catalog/wella-germaniya?page=all',
 'http://beautydiscount.ru/catalog/revlon-professional-ispaniya?page=all',
 'http://beautydiscount.ru/catalog/wella-system-professional-germaniya?page=all',
 'http://beautydiscount.ru/catalog/divage-rossiya?page=all',
 'http://beautydiscount.ru/catalog/hair-bobbles-daniya?page=all',
 'http://beautydiscount.ru/catalog/lancome-frantsiya?page=all',
 'http://beautydiscount.ru/catalog/kerastase-frantsiya?page=all',
 'http://beautydiscount.ru/catalog/lebel-yaponiya?page=all',
 'http://beautydiscount.ru/catalog/catrice-germaniya?page=all',
 'http://beautydiscount.ru/catalog/artdeco-germaniya?page=all',
 'http://beautydiscount.ru/catalog/korres-gretsiya?page=all',
 'http://beautydiscount.ru/catalog/lucas-papaw-remedies-avstraliya?page=all',
 'http://beautydiscount.ru/catalog/elf-ssha?page=all',
 'http://beautydiscount.ru/catalog/eos-ssha?page=all', 
 'http://beautydiscount.ru/catalog/essence-germaniya?page=all',
]

def main():
	for url in start_urls:
		vendor = url.split('/')[-1].split('?')[0]
		prc = Popen("scrapy crawl dmoz -o %s.csv -a start_url='%s'" % (vendor, url), shell=True)
		prc.wait()

if __name__=="__main__":
	main()
