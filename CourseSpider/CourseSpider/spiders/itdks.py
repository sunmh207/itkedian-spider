# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class ItdaksSpider(scrapy.Spider):
    name = 'itdks'
    site = 'it大咖说'.decode('utf-8')

    def start_requests(self):
        urls=[]
        sites = ['http://www.itdks.com']
        for site in sites:
            for i in xrange(1,5): 
                urls.append(site+'/dakalive?page='+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('div.event_list div.col-lg-3'):
            course = Course()
            #title
            title = section.css('div.infotip div.name::text').extract_first()
            if not title is None:
                course['title'] = title.strip()
            else:
                return

            #subtitle
            
            #about

            #price
            
            priceTxt = response.css('span.price::text').extract_first()
            if not priceTxt is None:
                if priceTxt.find('免费'.decode('utf-8')) > -1:
                    course['price'] = 0.0
                elif priceTxt.strip() == '':
                    course['price'] = 0.0
                else:
                    course['price'] = priceTxt.replace('￥'.decode('utf-8'),'').strip()

            #cover
            course['cover'] = response.urljoin(section.css('div.event_cover img.img_lazy::attr(data-original)').extract_first())
            #url
            course['url'] = response.urljoin(section.css('a::attr(href)').extract_first())
            
        
            #rating 
            #ratingN 
            #hitN 
            #ctype 
            course['ctype'] = 'V' #视频
            #site
            course['site'] = self.site 
            #tags 

            course['updated'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
        
            ###out
            
           
            #o_rating
            #o_price
            if not priceTxt is None:
                course['o_price'] = priceTxt.strip()
            #o_rating 
            #o_ratingN
            #o_stuN
            #o_reviewN
            
            #o_hitN
            request = scrapy.Request(url=course['url'], callback=self.parseDetail)
            request.meta['course'] = course

            yield request

    def parseDetail(self, response):
        course = response.meta['course']
        o_hitN = response.css('div.span_box span')[2].re(r'> (\d+)')
        if not o_hitN is None:
            course['o_hitN'] = int(o_hitN[0])
        print o_hitN
        yield course


class ItdaksLiveSpider(scrapy.Spider):
    name = 'itdks.live'
    site = 'it大咖说'.decode('utf-8')

    def start_requests(self):
        urls=['http://www.itdks.com']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('div.event_list div.col-ls-5'):
            live = Live()
            #title

            #subtitle
            
            #about

            #price
            
            #cover
            live['cover'] = response.urljoin(section.css('div.event_cover img::attr(src)').extract_first())
            #url
            live['url'] = response.urljoin(section.css('a::attr(href)').extract_first())
        
            #site
            live['site'] = self.site 
            #tags 

            yield live            
            