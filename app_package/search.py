#coding:utf-8
from flask import Flask , Blueprint , request 
import urllib2 , urllib
from bs4 import BeautifulSoup
search_blue = Blueprint("sb" , __name__)


@search_blue.route('/search' , methods=['POST' , 'GET'])
def search():
    # 将传过来的unicode字符编码成utf-8 , 然后在进行url编码
    bookname = urllib.quote(request.form.get('bookname').encode('utf-8'))
    search_url = "https://book.douban.com/subject_search?search_text=%s"%bookname

    #服务器欺骗-----------
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" , "Referer":"https://book.douban.com"}
    '''
    values =  {}
    data = urllib.urlencode(values)
    '''
    error_info ='''
        <div class="alert alert-warning alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>哎呦 !</strong>你搜索的书籍好像没什么 人气耶.... 
</div>'''
    #服务器欺骗-----------
    #构造请求
    try:
        req_s = urllib2.Request(search_url, headers=header)
        response_s = urllib2.urlopen(req_s)
        rec_s=response_s.read()
        ## 使用Python的内置标准库解析HTML
        soup = BeautifulSoup(rec_s , "html.parser")
    except:
        return error_info+"xxxxxxx"

    try:
        bookurl = soup.find('div' , class_='info').find('a')['href']
        req_b = urllib2.Request(bookurl , headers=header)
        response_b = urllib2.urlopen(req_b)
        rec_b = response_b.read()
        soup_b = BeautifulSoup(rec_b ,  'html.parser')
        title = str(soup_b.find('a' , class_='nbg')['title'])

        try:
            intro = str(soup_b.find('span' , class_='all hidden ').find('div' , class_='intro'))
        except:
            intro = str(soup_b.find('div' , class_='intro'))

        nbg = str(soup_b.find('a' , class_='nbg'))
        star = soup_b.find('strong' , class_='ll rating_num ').string
        author = soup_b.find('div' , id='info').find('a').string


        #try: 获取标签,无论是否能获取到内容,都会返回一个列表 即使是空列表
        user = soup_b.find_all('span' , class_='comment-info')
        content  = soup_b.find_all('p' , class_='comment-content')

        list_user = []
        for i in user:
            list_user.append(i)
        if not len(list_user):
            list_user.append("")

        list_content = []
        for j in content:
            list_content.append(j)
        if not len(list_content):
            list_content.append("目前还没有人评论这本书....")


        book1 = '''
        <div style="margin:0 auto ; background-color:#ffffff;width:90%%">
            <div style="float:left; width:60%%">
                <h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;《%s》</h1>
                <a style="float:right;width:70%%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br><br>豆瓣评分<span class="badge">%s</span></a>
            </div>
            %s
            <hr>
            <div>
                <h2>简介</h2>
                %s
            </div>
            <hr>
            <h2>读者评论</h2>
            '''%(title ,author , star , nbg , intro)

        book2  = ""
        for (x , y) in zip(list_user , list_content):
            book2 +='''
            <div class="panel panel-default">
                <div class="panel-body">
                    <div style="float:left">
                    %s
                    </div>
                    <div style="float:right">
                    %s
                    </div>
                </div>
            </div>
            '''%(y , x)
        book3 = "<br><hr><hr>"
        return book1+book2+book3
    except:
        return error_info





@search_blue.route('/today' , methods=['POST' , 'GET'])
def today():
    url = "https://book.douban.com/"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" , "Referer":url}


    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" , "Referer":url}
    req = urllib2.Request(url  ,headers=header )
    res = urllib2.urlopen(req)
    html = res.read()
    #soup = BeautifulSoup(open('a.html') , 'html.parser')
    soup = BeautifulSoup(html , 'html.parser')
    #print soup.head.title.string.encode(utf-8')
    ul = soup.body.find('ul' , class_="list-express")
    next_ul = ul.find_next_sibling('ul' , class_="list-express")
    img = next_ul.find_all('img')
    title = next_ul.find_all('h4')
    author = next_ul.find_all('div' , class_='author')
    if not len(author):
        author = "佚名"

    def lis(value):
        alist=[]
        for i  in value:
            alist.append(i)
        return alist
    
    
    lis_img = lis(img)

    lis_title = []
    for i in title:
        lis_title.append(i.string)
    lis_authoer = lis(author)

    tuijian = '''


<div id="today">
    <div class="row">
        <div  id="b1" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b1").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
        <div id="b2" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b2").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
        <div id="b3" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b3").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
        <div id="b4" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b4").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
        <div id="b5" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b5").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
        <div id="b6" class="col-sm-3 col-md-2">
            <div class="thumbnail">
                <script type="text/javascript">
                $(document).ready(function() {
                    $("#b6").click(function() {
                        $.post("/search", {
                                bookname: "%s"
                            },
                            function(data, status) {
                                $("#change").html(data);
                            })
                    });
                });

                </script>
                <a href="#">   %s</a>
                <div class="caption">
                    %s
                    <h6>%s</h6>
                </div>
            </div>
        </div>
    </div>
</div>



  '''%(lis_title[0].strip() ,lis_img[0],lis_title[0],lis_authoer[0],
       lis_title[1].strip() ,lis_img[1],lis_title[1],lis_authoer[1],
       lis_title[2].strip() ,lis_img[2],lis_title[2],lis_authoer[2],
       lis_title[3].strip() ,lis_img[3],lis_title[3],lis_authoer[3],
       lis_title[4].strip() ,lis_img[4],lis_title[4],lis_authoer[4],
       lis_title[5].strip() ,lis_img[5],lis_title[5],lis_authoer[5]
       )
    return tuijian