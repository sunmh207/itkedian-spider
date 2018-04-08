# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class MaizieduSpider(scrapy.Spider):
    name = 'maiziedu'
    site = '麦子学院'.decode('utf-8')

    def start_requests(self):
        urls=[]
        sites = ['http://www.maiziedu.com/course/web-all/0-',
                'http://www.maiziedu.com/course/python-all/0-',
                'http://www.maiziedu.com/course/ml-all/0-',
                ]
        for site in sites:
            for i in xrange(1,2): 
                urls.append(site+str(i)+'/')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('ul.course-lists li'):
            course = Course()
            #title
            title = section.css('p.font14::text').extract_first()
            if not title is None:
                course['title'] = title.strip()
            else:
                return

            #subtitle
            
            #about
            about = section.css('p.description::text').extract_first()
            if not title is None:
                course['about'] = about.strip()
           
            #price
            course['price'] = 0.0
            
            #cover
            course['cover'] = response.urljoin(section.css('p img::attr(src)').extract_first())
            #url
            course['url'] = response.urljoin(section.css('a::attr(href)').extract_first())
            
        
            #rating 
            #ratingN 
            #hitN 
            #ctype 
            course['ctype'] = 'N' #普通课程
            #site
            course['site'] = self.site 
            #tags 

            course['updated'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
        
            ###out
            
            #o_rating
            #o_price
      
            #o_rating 
            #o_ratingN
            #o_stuN
            o_stuN = section.css('p.color99::text').re(r'(\d+)')
            if not o_stuN is None:
                course['o_stuN'] = o_stuN
            #o_reviewN
        
            yield course
            