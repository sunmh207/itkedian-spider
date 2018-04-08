# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class ChinaHadoopSpider(scrapy.Spider):
    name = 'chinahadoop'

    def start_requests(self):
        urls=[]
        sites = ['http://www.chinahadoop.cn']
        for site in sites:
            for i in xrange(0,20):   #2017.08.21 max-course-id = 1018
                urls.append(site+'/course/list?page='+str(i))

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



'''
小象学院的班级
'''            
class ChinaHadoopClassroomSpider(scrapy.Spider):
    name = 'chinahadoop.classroom'

    def start_requests(self):
        urls=[]
        sites = ['http://www.chinahadoop.cn']
        for site in sites:
            for i in xrange(1,80):  #2017.08.21 max-course-id = 57
                urls.append(site+'/classroom/'+str(i)+'/introduction')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        course = Course()
        course['site'] = '小象学院'.decode('utf-8')
        title = response.css('h2.title::text').extract_first()
        if not title is None:
            course['title'] = title.strip()
        else:
            return

        #sbutitle
        #about

        course['cover'] = response.urljoin(response.css('div.class-img img::attr(src)').extract_first())
        course['url'] = response.url
            
        priceTxt = response.css('div.price span::text').extract_first()
        if not priceTxt is None:
            if priceTxt.find('免费'.decode('utf-8')) > -1:
                course['price'] = 0.0
            elif priceTxt.strip() == '':
                course['price'] = 0.0
            else:
                course['price'] = priceTxt.replace('元'.decode('utf-8'),'').strip()

        #rating 
        #ratingN 
        #hitN 
        #ctype 
        course['ctype'] = 'C'; #班级
        #site 
        #tags 
        course['updated'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
        
        #out
        if not priceTxt is None:
            course['o_price'] = priceTxt.strip()

        #o_rating
        o_starts = response.css('div.score i').re(r'class=\"es-icon (.*)\"')
        o_rating = 0
        for o_start in o_starts:
            if 'es-icon-star' == o_start:
                o_rating = o_rating + 2
            elif 'es-icon-starhalf' == o_start:
                o_rating = o_rating + 1
        course['o_rating'] = o_rating

        yield course    