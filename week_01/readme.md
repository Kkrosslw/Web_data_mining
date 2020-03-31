# :full_moon_with_face: Web数据挖掘第一节学了什么？
当然是爬虫啦嘿嘿:bug:
1. 认识requests_html :ok_woman:    
   这是最新的爬虫工具库，其中包含了request模块
2. 如何利用xpath和css定位 :ghost:    
   嘿嘿，小抄在这！:point_right: [xpath css定位速查表](https://blog.csdn.net/yaya_1q2w/article/details/79468098)   
   xpath比css定位更强大，有些xpath能做到的，css未必能
3. 上课的项目:blossom: 
   1. 抓取cnblogs新闻标题及链接
   2. 抓取猎聘工作
   3. jupyter notebook魔法之一：展示图，以及抓取bing图片  
   4. 利用状态狗的例子，来判断HTTP响应是否正常，使用了pd.read_html和requests+lxml两种不同的方法，pd.read_html只能碰碰运气，有时会怕不下来，状态狗的例子有说明。相比起这两种爬取方法，我更喜欢使用requests+xpath进行爬虫
   5. 同样还是状态狗的例子，用requests+lxml去爬取图片以及响应状态，最后下载图片
   6. 爬取豆瓣电影排行，使用pd.read_html失败了，改试requests+lxml，但是被反爬了！418！不要慌，我们要假装自己是浏览器，骗过网站，所以我们要加入头部信息，这样就可以顺利爬取到啦嘿嘿
   7.独角兽例子   
   [2019胡润全球独角兽榜]( https://www.hurun.net/CN/Article/Details?num=E7190250C866).爬取这个链接里的表格，使用pandas模块。
4. 同时我也举了一些例子:candy:  ：   
   1. 尝试爬取百度新闻网站（利用css定位）
   2. 尝试爬取猎聘网工作的薪资待遇（利用Xpath定位）
   3. 尝试抓取新浪图网图片（利用Xpath定位）
5. 最后是作业！:heavy_check_mark:   
  作业还是有一定难度，只能初步完成前三题，对requests+lxml的方式爬取数据不是非常熟悉，如果用requests_html+xpath我将会做的更好。
# :new_moon_with_face:学完本节课感想： 
### 爬虫真的有点好玩！就是对定位语法还不太熟练，需多加练习！ :stuck_out_tongue:
