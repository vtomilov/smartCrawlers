# -*- coding: utf-8 -*-
import scrapy
import random
import time
from subprocess import Popen

from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    taglist = [
            "крем",
            "гель",
            "для лица",
            "для волос",
            "для тела",
            "пудра",
            "лак",
            "для ногтей",
            "шампунь",
            "мыло",
            "для губ",
            "лосьон",
            "помада",
            "блеск",
            "тени",
            "тушь",
            "тональный",
            "бронзер",
            "румяна",
            "мицеллярная вода",
            "термальная вода",
            "хайлайтер",
            "для рук",
            "скраб",
            "карандаш",
            "для глаз",
            "для век",
            "бальзам",
            "палетка",
            "консилер",
            "корректор",
            "краска",
            "маска",
            "кисть",
            ]
    allowed_domains = ["beautydiscount.ru"]
    start_urls = []
    def __init__(self, start_url=None, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.handles = {}

 #    start_urls = [
# 'http://beautydiscount.ru/catalog/everyday-minerals-ssha?page=all',
# 'http://beautydiscount.ru/catalog/lumene-finlyandiya?page=all',
# 'http://beautydiscount.ru/catalog/pupa?page=all',
# 'http://beautydiscount.ru/catalog/opi-ssha?page=all',
# 'http://beautydiscount.ru/catalog/londa-germaniya',
# 'http://beautydiscount.ru/catalog/weleda-germaniya?page=all',
# 'http://beautydiscount.ru/catalog/rimmel-velikobritaniya?page=all',
# 'http://beautydiscount.ru/catalog/revlon-professional-ispaniya?page=all',
# 'http://beautydiscount.ru/catalog/maybelline?page=all',
# 'http://beautydiscount.ru/catalog/max-factor-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/anna-lotan-izrail?page=all',
 # 'http://beautydiscount.ru/catalog/anny-cosmetics-germaniya?page=all',
 # 'http://beautydiscount.ru/catalog/batiste-velikobritaniya-',
 # 'http://beautydiscount.ru/catalog/beauty-blender-ssha',
 # 'http://beautydiscount.ru/catalog/beauty-essential-rossiya',
 # 'http://beautydiscount.ru/catalog/biotherm-frantsiya?page=all',
 # 'http://beautydiscount.ru/catalog/crest_3d_white',
 # 'http://beautydiscount.ru/catalog/carmex-ssha',
 # 'http://beautydiscount.ru/catalog/embryolisse-frantsiya-?page=all',
 # 'http://beautydiscount.ru/catalog/dose-of-colors-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/helena-rubinstein-avstraliya?page=all',
 # 'http://beautydiscount.ru/catalog/invisibobble-?page=all',
 # 'http://beautydiscount.ru/catalog/japan-gals-yaponiya?page=all',
 # 'http://beautydiscount.ru/catalog/mythic-oil---dlya-zaschity',
 # 'http://beautydiscount.ru/catalog/hairchalk---makiyazh-dlya-volos',
 # 'http://beautydiscount.ru/catalog/lime-crime-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/lucas-papaw-remedies-avstraliya',
 # 'http://beautydiscount.ru/catalog/macadamia-natural-oil-ssha',
 # 'http://beautydiscount.ru/catalog/mizon-koreya?page=all',
 # 'http://beautydiscount.ru/catalog/moroccanoil-izrail?page=all',
 # 'http://beautydiscount.ru/catalog/missha-koreya?page=all',
 # 'http://beautydiscount.ru/catalog/nyx-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/organic-shop-rossiya?page=all',
 # 'http://beautydiscount.ru/catalog/redken-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/sally-hansen-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/sleek_makeup?page=all',
 # 'http://beautydiscount.ru/catalog/tangle-teezer-velikobritaniya?page=all',
 # 'http://beautydiscount.ru/catalog/thebalm-ssha-?page=all',
 # 'http://beautydiscount.ru/catalog/tony-moly-koreya?page=all',
 # 'http://beautydiscount.ru/catalog/yves-saint-laurent-frantsiya?page=all',
 # 'http://beautydiscount.ru/catalog/wet-and-wild-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/real-techniques-ssha',
 # 'http://beautydiscount.ru/catalog/wella-germaniya?page=all',
 # 'http://beautydiscount.ru/catalog/revlon-professional-ispaniya?page=all',
 # 'http://beautydiscount.ru/catalog/wella-system-professional-germaniya?page=all',
 # 'http://beautydiscount.ru/catalog/divage-rossiya?page=all',
 # 'http://beautydiscount.ru/catalog/hair-bobbles-daniya?page=all',
 # 'http://beautydiscount.ru/catalog/lancome-frantsiya?page=all',
 # 'http://beautydiscount.ru/catalog/kerastase-frantsiya?page=all',
 # 'http://beautydiscount.ru/catalog/lebel-yaponiya?page=all',
 # 'http://beautydiscount.ru/catalog/catrice-germaniya?page=all',
 # 'http://beautydiscount.ru/catalog/artdeco-germaniya?page=all',
 # 'http://beautydiscount.ru/catalog/korres-gretsiya?page=all',
 # 'http://beautydiscount.ru/catalog/lucas-papaw-remedies-avstraliya?page=all',
 # 'http://beautydiscount.ru/catalog/elf-ssha?page=all',
 # 'http://beautydiscount.ru/catalog/eos-ssha?page=all', 
 # 'http://beautydiscount.ru/catalog/essence-germaniya?page=all',
 #    ]
                                      
#response.xpath('//div[@class="product product_on_sale_page"]/div[@class="product_info"]').xpath('h3/a/span/text()').extract()                     
    def parse(self, response):
        self.sku = 21424
        for sel in response.xpath('//div[@class="product product_on_sale_page"]'):
            item = DmozItem()
            title = sel.xpath('div[@class="product_info"]/h3/a/span/text()').extract_first()
            item['Title'] = title
            handle = '-'.join(title.lower().split())
            if self.handles.has_key(handle):
                self.handles[handle] += 1
                handle += '-' + str(self.handles[handle])
            else:
                self.handles[handle] = 1

            Image_Src = sel.css('img').xpath('@src').extract_first().split('?')[0]
            item['Handle'] = handle
            fname = Image_Src.split('/')[-1]
            res = ""
            c = 0
            s = fname
            while c < len(s):
    		if s[c] != '%':
        	    res += s[c]
    		else:
        	    if s[c:c+3] == '%20':
            		res += '_'
        	    c += 2
    		c+=1
            #result = ""
            #c = 0
            #while c < len(res):
            #    result += res[c]
            #    while res[c] == "_" and c < len(res):
            #        c+=1

            item['Image_Src'] = "https://cdn.shopify.com/s/files/1/1316/6641/files/" + res
            item['Vendor'] = " ".join(response.request.url.split('/')[-1].split('?')[0].split('-')[:-1]).title()
            self.dl(Image_Src)
            item['Description'] = sel.xpath('div[@class="product_info"]/h3/a/text()[2]').extract_first().strip()
            price = int(sel.xpath('div[@class="product_info"]//tr[@class="variant"]//span[@class="price"]/text()').extract()[0].replace(" ", ""))
            price = int(1.05 * price)
            item['Price'] = price
            item['Type'] = 'Cosmetics'
            item['SKU'] = self.sku
            
            item['Quantity'] = random.randint(1, 20)
            self.sku += 1
            yield item

    def dl(self, url):
        time.sleep(0.01)
        prc = Popen("wget -P /Users/vtomilov/Downloads/scrapy_venv/tutorial/images/ %s" % url, shell=True)
        prc.wait()
