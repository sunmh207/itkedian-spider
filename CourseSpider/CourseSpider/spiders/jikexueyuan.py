# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class JikexueyuanSpider(scrapy.Spider):
    name = 'jikexueyuan'
    site = '极客学院'.decode('utf-8')

    def start_requests(self):
        urls=[]
        sites = ['http://www.jikexueyuan.com/']
        for site in sites:
            for i in xrange(1,2): 
                urls.append(site+'course/?pageNum='+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for section in response.css('div.lesson-list ul.cf li'):
            course = Course()
            #title
            title = section.css('div.lesson-infor h2.lesson-info-h2 a::text').extract_first()
            if not title is None:
                course['title'] = title.strip()
            else:
                return

            #subtitle
            subtitle = section.css('div.lesson-infor p::text').extract_first()
            if not subtitle is None:
                course['subtitle'] = subtitle.strip()
            
            #about
            #price
            #cover
            course['cover'] = section.css('div.lessonimg-box a img::attr(src)').extract_first()
            #url
            course['url'] = section.css('div.lessonimg-box a::attr(href)').extract_first()
            
        
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
            o_stuN = section.css('div.lesson-infor em.learn-number').re(r'(\d+)')
            if not o_stuN is None:
                course['o_stuN'] = int(o_stuN[0])
            #o_reviewN
        
            yield course
            