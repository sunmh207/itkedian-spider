# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class EggheadSpider(scrapy.Spider):
    name = 'egghead'
    site = 'egghead'.decode('utf-8')

    def start_requests(self):
        urls=['https://egghead.io/courses']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('div.card-course-inner'):
            course = Course()
            #title
            title = section.css('div.card-content div.course-description-holder div.condensed-card-only h3.course-title span::text').extract_first()
            if not title is None:
                course['title'] = title.strip()
            else:
                return

            #subtitle
            
            #about

            #price
            
            #cover
            course['cover'] = response.urljoin(section.css('div.card-content div.course-image-holder img::attr(src)').extract_first())
            #url
            course['url'] = response.urljoin(section.css('div.card-content a.link-overlay::attr(href)').extract_first())
            
        
            #rating 
            #ratingN 
            #hitN 
            #ctype 
            course['ctype'] = 'N' #普通
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
            #o_reviewN
        
            yield course

