# :blue_heart: :purple_heart: 本周学了什么？
## :feet: 一、回顾上周学的内容
1. 上周老师带我们认识了requests-html库，requests也包含在requests-html中
2. 还认识了pd.read_html和requests+lxml，其中pd.read_html在爬取数据时只能碰碰运气，不是啥都能顺利爬下来
3. 使用状态狗的例子来判断HTTP状态及HTTP响应是否正常，同时判断会不会被反爬（如代码418）
## :snail: 二、本周学习内容
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
7. 用xpath在网页进行定位时，可以找比较靠前的元素，利用他们的属性进行快速定位，不用在路径上都得详细他们的标签，要懂得优化路径
8. 还将爬取出来的数据导入excel里，利用pd.to_excel()做到
## :baby_chick:三、关于加分项那些事儿
1. C-3 :blush:  
C-3是最简单的题目，直接按照xpath的语法将选择器、属性啥的输进去就可以爬取。老师给的链接会自动定位，而我的城市并没有关于pandas的工作，刚开始一直爬取不到，我还以为是我前几天爬取太多次被liepin拉黑了，后来才发现是定位的问题，所以我将老师给的链接替换为不限地区的链接，便可以轻松爬取到啦！   
2. C-4 :disappointed_relieved:   
这道题对我来说有点难度，刚开始我把要爬取的公司、地点用xpath语法输入后，出现报错，而只爬取其中一个的话可以成功爬取，这说明我的代码并没有问题，于是我认真查看了报错信息，原来是两组的长度不同。[丘天惠](https://github.com/Autumnhui)同学提示我可以把他们长度打印出来看看，于是我用len函数打印了他们的长度之后，发现了问题，因为有推广广告的存在，只要删去推广广告的就可以，照着这个思路，最后就可以成功爬取到啦！   
3. C-5 :cold_sweat:   
哇这道题真的是难倒我了，我用了strip、''.join()等各种函数去删除其中一个变量的空格符和\n，都没有成功，最后请教了[丘天惠](https://github.com/Autumnhui)同学,他给我发了一个博客的链接，最后才可以解决。这道题真的多亏了靓仔丘天惠给我提示，不然我都做不出来。   
## :tropical_fish: 四、本周的总结
我越来越喜欢这门课啦，真真实实地体会到了爬虫的乐趣，爬虫可比写代码有趣多了，经过本周的学习，我对xpath的语法也进一步地熟悉了，当然还是要多多学习！ **多多学会看报错信息，for循环的推导式要加强联系，爬取网页时多注意元素的节点，多观察页面结构。** 不要因为遇到报错就变得急躁，要冷静处理一切问题。最后超级感谢同学给予的提醒与帮助，超级谢谢老师给我们上这门课和给我们超多的学习资源嘿嘿:last_quarter_moon_with_face:
