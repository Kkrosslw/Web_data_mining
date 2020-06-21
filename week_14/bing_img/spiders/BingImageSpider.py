# -*- coding: utf-8 -*-
import scrapy
from bing_img.items import BingImgItem
import pandas as pd
import json

url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1592720152828&pid=hp"

from urllib.parse import urlparse, parse_qs, urlencode
from time import time

def parse_url_qs(url):
    six_parts = urlparse(url)
    out = parse_qs(six_parts.query)
    return (out,six_parts)
参数, six = parse_url_qs (url)

参_template = 参数.copy()

def get_url_byN(N):
    参_template['idx'] = [str(N)]
    参_template['ts'] = [int(time())]
    q = urlencode(参_template, doseq = True) # doseq = True
    six_new = six._replace(query=q)
    u = six_new.geturl()
    return (u,six_new)

start_urls = []
for i in range(8):
    u,s = get_url_byN(N=i)
    start_urls.append(u)
    

class BingimagespiderSpider(scrapy.Spider):
    name = 'BingImageSpider'
    allowed_domains = ['cn.bing.com']
    start_urls = start_urls

    def parse(self, response):
        # 更改 debug
        r_json = json.loads(response.body.decode("utf8"))
        df = pd.json_normalize(r_json['images'])
        ulist = list(df.loc[:,'url'])
        copyrights = list(df.loc[:,'copyright'])
        
        if len(ulist)>0:
            
            url_list = []
            copy_list = []
            for u in ulist:
                url_list.append("https://cn.bing.com{q}".format(q=u))
            for copy in copyrights:
                copy_list.append(copy)
        item = BingImgItem()
        item['image_urls'] = url_list
        item['copys'] = copy_list
        yield (item)

