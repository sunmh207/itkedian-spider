# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class ChinaHadoopSpider(scrapy.Spider):
    name = 'imooc'

    def start_requests(self):
        urls=[]
        sites = ['http://www.imooc.com']
        for site in sites:
            for i in xrange(1,2):   
                urls.append(site+'/course/list?c=cb&page='+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('div.course-item'):
            course = Course()
            course['site'] = '小象学院'.decode('utf-8')
            title = section.css('div.course-info div.title a::text').extract_first()
            if not title is None:
                course['title'] = title.strip()
            else:
                return

            #sbutitle
            #about

            #cover
            course['cover'] = response.urljoin(section.css('div.course-img a img::attr(src)').extract_first())
            course['url'] = response.urljoin(section.css('div.course-img a::attr(href)').extract_first())

            #price
            freeTxt = section.css('span.price span.text-danger::text').extract_first()
            if not freeTxt is None:
                course['price'] = 0.0
            else: 
                priceTxt = section.css('span.price::text')[1].extract() 
                if not priceTxt is None:   
                    course['price'] = priceTxt.strip()

            #rating 
            #ratingN 
            #hitN 
            #ctype 
            course['ctype'] = 'N'; #普通课程
            #site 
            #tags 
            course['updated'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())

            #out
            #o_rating
            #o_starts
            #o_stuN
            o_stuN = section.css('span.num::text').re(r'(\d+)')
            if not o_stuN is None:
                course['o_stuN'] = int(o_stuN[0])

            yield course
   