# -*- coding: utf-8 -*-
BOT_NAME = 'CourseSpider'
SPIDER_MODULES = ['CourseSpider.spiders']
NEWSPIDER_MODULE = 'CourseSpider.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 5
ITEM_PIPELINES = {
  'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 300,
}
ELASTICSEARCH_SERVERS = ['http://localhost:9200']
ELASTICSEARCH_INDEX = 'course'
ELASTICSEARCH_TYPE = 'c'
ELASTICSEARCH_UNIQ_KEY = 'url'
ELASTICSEARCH_USERNAME = 'elastic'
ELASTICSEARCH_PASSWORD = 'elastic'
