# :no_mouth: What do we learn in week3 ?
## 一、本周内容:two_women_holding_hands:
1. 对上周的加分项进行讲解以及进一步挖掘数据。其中用到了函数和高级列表推导（内心os:老师写的代码实在是太精炼了，我啃了好久才把代码啃下去）
2. 接着对公司进行一个“分类”，每个公司对应的类型是什么，比如：“中国500强”、“2018互联网300强”等。   
   * 首先，先获取每个公司类型的url，并存入字典中
   * 对上述url进行解析，使用urllib进行解析。urlparse解析后会返回6个部分，分别是scheme（机制）、netioc（网络位置）、path（路径）、params（路径段参数）、query（查询）、fragment（片段）   
   * 解析完url后，返回的数据还是很长，我们需要是要使用nuninque进行相异值计量对比，看看返回的数据哪里有不同
   * 接着，我们就看到了query有不同，我们再对query进行进一步解析，使用parse_qs进行解析
3. 对url的参数解析完成之后，就要构建参数模板和参数字典
4. 准备爬取多个页面的数据：准备好url和params，然后进行请求，for循环每一页的数据，将其爬取下来，用我们最开始解析的url去获取更多的url
## 二、总结:speak_no_evil:	
:cry:本来前两周还感受到爬虫的乐趣，非常快乐，结果这一周的代码给我当头一棒，老师写的代码逻辑太强，一时有点懵，啃了很久才勉强啃下去，哭了。本周的重点主要是在对url和query的解析，以及爬取多个页面的数据，生成网页连续
技。参数模板的生成对于爬取页面十分重要，有了模板我们便能源源不断的爬取每一页数据，而且我们用的是参数字典（老师说用参数字典更高级）。虽然老师写的代码每一步都很详细，但是对于我这种菜鸟来说还是有点难，继续加油！我一定要好好学这门课！！！
