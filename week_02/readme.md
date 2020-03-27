# 本周学了什么？
## 一、回顾上周学的内容
1. 上周老师带我们认识了requests-html库，requests也包含在requests-html中
2. 还认识了pd.read_html和requests+lxml，其中pd.read_html在爬取数据时只能碰碰运气，不是啥都能顺利爬下来
3. 使用状态狗的例子来判断HTTP状态及HTTP响应是否正常，同时判断会不会被反爬（如代码418）
## 二、本周学习内容
1. 继续学习如何爬取网页，采用requests-html库爬取，使用xpath语法
2. 如何将网页存为文字档，可通过r.html.html做到，其中r.html是个类
3. 熟悉xpath语法，更深入了解该如何运用
4. 将python数据分析的pd.dataframe运用到数据挖掘上，更好地呈现数据爬取结果
5. HTML文本的解析，有两种方法   
   ```
   第一种方法
   import requests_html
   parsed = requests_html.soup_parse(html_load)
   ```
   ```
   第二种方法
   from requests)html import soup_parse
   parsed = soup_parse(html_load)
   ```
   6. greedy和ungreedy
   greedy指“不挑剔”标签地去进行数据爬取，ungreedy指有针对性的、“挑剔的”去爬取我们想要的数据
