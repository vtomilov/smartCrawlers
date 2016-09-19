# -*- coding: utf-8 -*-
import scrapy
import random
import time
from subprocess import Popen, PIPE
import os
from transliterate import translit, get_available_language_codes
import urllib
import re

from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    
    allowed_domains = ["beautydiscount.ru"]
    start_urls = []
    def __init__(self, start_url=None, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.handles = {}
        self.cnt = 32
        self.sku = 15000
        self.uni2ascii = {
            u'\xe2\x80\x99': u"'",
            u'\xe2\x80\x9c': u'"',
            u'\xe2\x80\x9d': u'"',
            u'\xe2\x80\x9e': u'"',
            u'\xe2\x80\x9f': u'"',
            u'\xc3\xa9': u'e',
            u'\xe2\x80\x9c': u'"',
            u'\xe2\x80\x93': u'-',
            u'\xe2\x80\x92': u'-',
            u'\xe2\x80\x94': u'-',
            u'\xe2\x80\x94': u'-',
            u'\xe2\x80\x98': u"'",
            u'\xe2\x80\x9b': u"'",

            u'\xe2\x80\x90': u'-',
            u'\xe2\x80\x91': u'-',

            u'\xe2\x80\xb2': u"'",
            u'\xe2\x80\xb3': u"'",
            u'\xe2\x80\xb4': u"'",
            u'\xe2\x80\xb5': u"'",
            u'\xe2\x80\xb6': u"'",
            u'\xe2\x80\xb7': u"'",

            u'\xe2\x81\xba': u"+",
            u'\xe2\x81\xbb': u"-",
            u'\xe2\x81\xbc': u"=",
            u'\xe2\x81\xbd': u"(",
            u'\xe2\x81\xbe': u")",
            }

 
                                      
#response.xpath('//div[@class="product product_on_sale_page"]/div[@class="product_info"]').xpath('h3/a/span/text()').extract()                     
    def parse(self, response):
        for sel in response.xpath('//div[@class="product product_on_sale_page"]'):
            item = DmozItem()
            title = sel.xpath('div[@class="product_info"]/h3/a/span/text()').extract_first()
            item['Title'] = title
            handle = self.translit(title)
            if self.handles.has_key(handle):
                self.handles[handle] += 1
                handle += '-' + str(self.handles[handle])
            else:
                self.handles[handle] = 1

            Image_Src = sel.css('img').xpath('@src').extract_first().split('?')[0]
            item['Handle'] = handle
            dirname = 1

            fname = Image_Src.split('/')[-1]
            defaultName = False
            try:
                fname = urllib.unquote(fname)
            except UnicodeEncodeError:
                print (u"Can't decode %s" % Image_Src)
                dirname = 100
                defaultName = True

            d = "/Users/vtomilov/Downloads/scrapy_venv/tutorial/images/%s/" % dirname
            if (not os.path.exists(d)):
                os.mkdir(d)

            while (len(os.walk("/Users/vtomilov/Downloads/scrapy_venv/tutorial/images/%s/" % dirname).next()[2]) >= 100):
                dirname += 1
                d = "/Users/vtomilov/Downloads/scrapy_venv/tutorial/images/%s/" % dirname
                if (not os.path.exists(d)):
                    os.mkdir(d)

            fname = self.dl(Image_Src, dirname)
            fname = fname.replace("(", "").replace(")", "")
            fname = self.translit(fname)
      #       res = ""
      #       c = 0
      #       s = fname
      #       while c < len(s):
    		# if s[c] != '%':
      #   	    res += s[c]
    		# else:
      #   	    if s[c:c+3] == '%20':
      #       		res += '_'
      #   	    c += 2
    		# c+=1
            #result = ""
            #c = 0
            #while c < len(res):
            #    result += res[c]
            #    while res[c] == "_" and c < len(res):
            #        c+=1

            item['Image_Src'] = "https://cdn.shopify.com/s/files/1/1316/6641/files/" + fname
            item['Vendor'] = " ".join(response.request.url.split('/')[-1].split('?')[0].split('-')[:-1]).title()

            
            item['Description'] = sel.xpath('div[@class="product_info"]/h3/a/text()[2]').extract_first().strip()
            price = int(sel.xpath('div[@class="product_info"]//tr[@class="variant"]//span[@class="price"]/text()').extract()[0].replace(" ", ""))
            price = int(1.05 * price)
            item['Price'] = price
            item['Type'] = 'Cosmetics'
            item['SKU'] = self.sku
            
            item['Quantity'] = random.randint(1, 20)
            self.sku += 1
            yield item

    def dl(self, url, dirname):
        time.sleep(0.01)
        d = "/Users/vtomilov/Downloads/scrapy_venv/tutorial/images/%s/" % dirname
        prc = Popen("wget -P %s %s" % (d, url), shell=True, stderr=PIPE, stdout=PIPE)
        out, err = prc.communicate()
        err = unicode(err, errors='ignore')
        fname = re.search("Saving to: (.+)", err, flags=re.UNICODE).group(1)
        for key, value in self.uni2ascii.items():
            try:
                fname = fname.replace(key, value)
            except UnicodeDecodeError:
                print(fname, type(fname))
                print(key, value)
                print(type(key), type(value))
                assert(False)
        fname = fname.decode('utf8')[1:].split('/')[-1]
        # pattern = re.compile('|'.join(self.uni2ascii.keys()), flags=re.UNICODE)
        # fname = pattern.sub(lambda x: self.uni2ascii[x.group()], fname).decode('utf8')[1:-1].split('/')[-1]
        return fname


    def translit(self, arg):
        return '-'.join(translit(arg, 'ru', reversed=True).split())



