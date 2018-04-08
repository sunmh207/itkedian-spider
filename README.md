# itkedian-spider
IT课店, 发现好课程 https://www.itkedian.com/

爬虫模块的源代码

## 简介
这是一个基于scrapy框架的爬虫，它会访问指定网站的课程，并把课程信息存储到Elasticsearch中。

## 安装

### 安装 Elasticsearch

参见 https://www.elastic.co/cn/downloads
安装并启动后，保证http://localhost:9200 能够访问

### 安装scrapy

```
pip install scrapy
```

### 安装 scrapyelasticsearch 包

```
pip install ScrapyElasticSearch
```

### 下载itkedian爬虫代码

```
git clone https://github.com/sunmh207/itkedian-spider.git
```

### 运行

命令格式为: scrapy crawl <爬虫name>, 如
```
cd CourseSpider
scrapy crawl jikexueyuan
```
爬虫会扫描该网站的课程，并存储到elasticsearch的索引中。



