# -*- coding: utf-8 -*-
import scrapy
from CourseSpider.items import Course
from time import gmtime, strftime

class OsforceSpider(scrapy.Spider):
    name = 'osforce'

    def start_requests(self):
        urls=[]
        sites = ['http://www.osforce.cn']
        for site in sites:
            for i in xrange(400,600): 
                urls.append(site+'/course/'+str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        course = Course()
        course['site'] = '开源力量'.decode('utf-8')
        title = response.css('h2.title::text').extract_first()
        if not title is None:
            course['title'] = title.strip()
        else:
            return

        #sbutitle
        #about
        course['cover'] = response.urljoin(response.css('div.course-img img::attr(src)').extract_first())
        course['url'] = response.url

        priceTxt = response.css('span.price::text').extract_first()
        if not priceTxt is None:
            if priceTxt.find('免费'.decode('utf-8')) > -1:
                course['price'] = 0.0
            else:
                course['price'] = priceTxt.replace('元'.decode('utf-8'),'').strip()

        #rating 
        #ratingN 
        #hitN 
        #ctype
        course['ctype'] = 'N'; #普通课程
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

        
        

        #o_ratingN
        o_ratingN = response.css('div.score span').re(r'(\d+)')
        if not o_ratingN is None:
            course['o_ratingN'] = int(o_ratingN[0])


        #o_stuN 
        o_stuN = response.css('div.student-num::text').re(r'(\d+)')
        if not o_stuN is None:
            course['o_stuN'] = int(o_stuN[0])
        #adm
        #adm_rating

        return course

class OsforceGoodSpider(OsforceSpider):
    name = 'osforce.good'
    o_rating_threshold = 8; #评分小于8分,不收集
    o_ratingN_threshold = 10; #小于10人评价,不收集

    def parse(self, response):
        course = super(OsforceGoodSpider,self).parse(response)
        if self.isGood(course):
            yield course


    def isGood(self,course):
        if course['o_rating'] < self.o_rating_threshold:
            return False
        if course['o_ratingN'] < self.o_ratingN_threshold:
            return False
        return True     
