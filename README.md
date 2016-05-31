爬虫练习

flask \ bootstrap \ AJAX \ JavaScript \ BeautifulSoup 

爬取豆瓣读书 https://book.douban.com/ 的新书速递 第二页 十本书(豆瓣图书 , 评论 是随机排列的,每次爬取不一样) 并在首页展示 , 且提供点击弹出图书详情

提供搜索功能 , 输入书名后系统进入豆瓣搜索页 https://book.douban.com/subject_search?search_text=%s  , 获取第一个搜索结果后系统进入书籍详情页 , 爬取包括标题等各种信息并AJAX返回展示至前端

自定义404



首页
![image](https://github.com/hadesong/dbooks/raw/master/app_package/static/1.jpg)

详情页
![image](https://github.com/hadesong/dbooks/raw/master/app_package/static/2.jpg)


未完成:
1\提交请求时的等待画面(等待AJAX返回结果 ,  大约3-5秒钟)

2\做书籍评论数少于6条或没有评论的判断 , 并相应处理