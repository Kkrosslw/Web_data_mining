# :full_moon_with_face:项目名称：爬取猎聘深圳地区热门编程行业的薪资
# :earth_americas:数据加值宣言
本项目产出按requests+xpath模块对猎聘深圳地区的IT互联网行业当下热门编程岗位（python岗、Java岗、PHP岗、C语言岗）的基本信息进行数据挖掘，以解决编程语言岗在当下社会环境的发展前景问题。
- 关键词：python、Java、PHP、C语言
- 页数：各10页
- 行业细分：互联网/电商、游戏产业、；计算机软件、IT服务
- 数据：共6400条

# :ghost:数据加值
- 产品核心加值：通过分析以上四门编程语言相关岗位的薪资，获取不同编程岗的薪资数据，再将薪资拆分成**最低月薪**、**最高月薪**、**平均月薪**进行进一步分析。
- 依本产品总结：
   - 以上四种热门编程岗位的最低薪资都很可观，最低薪资为8k-9k。
   - python岗、C语言岗最高月薪6w，Java岗最高月薪为6.5w，PHP岗最高月薪为7w，其中最高月薪达到以上四种水平的为游戏产业行业占比较多。
   - 就目前数据来看，游戏行业目前需要的PHP岗和C语言岗人才较多，但游戏产业用人需求还是以C语言（包括C语言衍生出来的C++/C#）岗为多数，原因之一是用C语言写游戏脚本和做嵌入式的公司企业较多。
   - IT服务、计算机软件行业用人需求较多的位Java岗和C语言岗。
   - 虽然PHP岗位不论是最高月薪，或是最低平均月薪，亦或是最高平均月薪，都比python岗位的高。但就目前社会情况来看，python比PHP岗更有发展前景，一是以为python可以做的东西比PHP更多，二是因为PHP官方已经停止了维护，三是因为python的网络架构、模块管理、可读性等比PHP更强。
   - 现在虽然很多网站依旧用PHP语言开发，但大型网站都是用C语言（包括C语言衍生出来的C++/C#）和Java写的，并且因现在PHP官方已不再进行更新维护且受到python、Go这些新兴语言的冲击，PHP的份额正在缓慢下降，有被其他语言的趋势。
   - 就目前的数据来看，PHP的薪资完胜Java和python，但其发展趋势却不如Java和python。

# :fries:挖掘Query参数
- industries 行业
- dqs 城市编码
- curpage 页码

# :new_moon_with_face:文件说明
- ```final.ipynb```为代码文档
- ```热门编程语言.xlsx```为最原始爬取下来的数据，共6400条
- ```热门编程语言_新.xlsx```为处理后的数据，新增了**最高月薪、最低月薪、平均年薪**栏位，共6400条
- ```编程岗薪资.html```为最后的数据可视化图，展示了4种编程岗位的薪资
