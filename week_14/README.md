## 认识新模块：Scrapy
1. Scrapy是一个爬虫框架，可快速抓取网页内容
2. Scrapy架构包括 引擎、调度器、下载器、爬虫、管道、下载中间件、Spider中间件
## 如何开始？
1. 导入模块
```
import scrapy
```
2. 创建Scrapy项目   
这里需注意，运行该命令的文件应与scrapy.cfg保持同一层级
```
! scrapy startproject 项目名称
```
3. 创建爬虫蜘蛛
```
! scrapy genspider 爬虫 "网站域名"
```
4. 修改上述该命令自动生成的文件
   * Spider文件夹下的py文件，需将我们写好的代码放进去
   * items.py文件
   * settings.py文件
   * 其他文件根据个人需要进行修改
5. 运行爬虫
```
! scrapy crawl 爬虫
```
