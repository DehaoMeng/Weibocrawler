# 网友对疫情防控的态度分析

[toc]  

## 一、设计目标

1. 爬取新浪微博中关于上海疫情的新闻评论信息。

2. 利用词云库对这些词进行词云分析

3. 对分析的数据结果进行图形化显示

## 二、关键问题

1．选取新闻网站，解析网页获取具体新闻评论信息

2．将获得的信息保存至txt和excel文件

3．数据分析处理及图形展示

## 三、整体构思和设计

1. 分别设计爬虫部分与数据处理部分

## 四、模块设计

### 4.1爬虫设计

对网站内容进行分析，并获取具体新闻评论相关信息，

### 4.2数据处理及图形化处理

对获取的新闻内容，进行分析，将前15位高频词汇以柱形图显示，所有词以词云图显示。

### 4.3数据保存

实现将数据保存至excel和txt文件的方法。

### 4.4主函数

通过“if“__name__”==“__main__”:“入口开始程序执行，依次调用实现程序功能。

## 五、运行结果和调试

![文本中度可信度描述已自动生成](file:////Users/dehaomeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image001.png)

<center>5.1评论爬取成功通知

![图形用户界面,文本,应用程序描述已自动生成](file:////Users/dehaomeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.png)

<center>5.2评论所有信息保存至excel和txt文件

![文本,白板描述已自动生成](file:////Users/dehaomeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image003.png)

<center>5.3词云图

![图表,条形图,直方图描述已自动生成](file:////Users/dehaomeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.png)

<center>5.4柱状图

![图形用户界面,文本,应用程序描述已自动生成](file:////Users/dehaomeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.png)

<center>5.5requirement.txt保存程序涉及到的库

## 六、心得体会

通过本次实验，深刻了解了网络爬虫机制与反爬虫机制，cookie登录信息保存等，使用数据分析时了解了pandas、wordcloud等多种方法的实现与功能定义。

通过本次调查也可以了解到，网友对上海疫情的关心以及对疫情防控的支持态度与对美好明天的祝愿。网友们在面对疫情没有颓废与对困难的畏惧。生活的热爱以及对政策的支持是毋庸置疑的。

# 附录：代码

## 源代码

### config.py

配置文件，其中包含微博登陆cookie和爬取的信息网址以及存储路径。

~~~python
#微博新闻信息网址
base_url='https://m.weibo.cn/status/'
#微博评论信息保存网址
url='https://m.weibo.cn/comments/hotflow?id='
#txt文件保存路径
txt_name='./comments/weibo_comments.txt'
ALF=1583630252
MLOGIN=1
M_WEIBOCN_PARAMS='oid%3D4469046194244186%26luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803'
SCF='AjheAPuZRqxmyLTkTVnBXGduebXE6nZGT5fS8_VPbfADyWHQ_WyoRzZqAJNujugOFYP1tUivrlzK2TGTx83_Qo.'
SSOLoginState=1581038313
SUB='_2A25zOMq5DeRhGeNM6FUX8S_EzDqIHXVQwtbxrDV6PUJbktAKLVPhkW1NTjKs6wgXZoFv2vqllQWpcwE-e9-8LlMs'
SUBP='0033WrSXqPxfM725Ws9jqgMF55529P9D9W58TWlXMj17lMMvjhSsjQ1p5JpX5K-hUgL.Fo-Ee0MceK2RS0q2dJLoIEXLxKqLBozL1h.LxKML1-BLBK2LxKML1-2L1hBLxK-LBKqL12BLxK-LBKqL12Bt'
SUHB='0BLYTPzIKSGsDo'
WEIBOCN_FROM=1110006030
XSRF_TOKEN='5dcf70'
_T_WM=64204543757
Cookie={
'Cookie':"weibo_cookie",#获取登录状态的cookie值
}
#头部信息
headers={
'Sec-Fetch-Mode':'cors',
'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/71.0.3578.98Safari/537.36',
'X-Requested-With':'XMLHttpRequest',#通过ajax请求形式获取数据
'X-XSRF-TOKEN':'aa8bed',
'Accept':'application/json,text/plain,/'
}
#数据id号，要爬取的微博的id号，以及导出到excel对应的sheet名
weiboComment=[{
'id':1,
'weibo_id':4775326871978967,
'sheet_name':'file_tab1',
'excel_name':r'./comments/weibo_comments1.xls'
},{
'id':2,
'weibo_id':4775440936339631,
'sheet_name':'file_tab1',
'excel_name':r'./comments/weibo_comments2.xls'
},{
'id':3,
'weibo_id':4775131773930646,
'sheet_name':'file_tab1',
'excel_name':r'./comments/weibo_comments3.xls'
},{
'id':4,
'weibo_id':4778915023822520,
'sheet_name':'file_tab1',
'excel_name':r'./comments/weibo_comments4.xls'
},{
'id':5,
'weibo_id':4770173918380517,
'sheet_name':'file_tab1',
'excel_name':r'./comments/weibo_comments5.xls'
}]
#忽略pandas调用警告信息
importwarnings
warnings.simplefilter(action='ignore',category=FutureWarning)
~~~

### weibo.py

包含主函数，调用config.py以及data_process.py，爬虫以及信息存储等部分代码。

~~~python
importrequests
importpandasaspd
importtime
fromconfigimportheaders,url,Cookie,base_url,weiboComment,txt_name
importdata_process

#将中国标准时间(SatMar1612:12:03+08002019)转换成年月日
defformatTime(time_string,from_format,to_format='%Y.%m.%d%H:%M:%S'):
time_struct=time.strptime(time_string,from_format)
times=time.strftime(to_format,time_struct)
returntimes
#爬取第一页的微博评论
deffirst_page_comment(weibo_id,url,headers):
try:
url=url+str(weibo_id)+'&mid='+str(weibo_id)+'&max_id_type=0'
web_data=requests.get(url,headers=headers,cookies=Cookie,timeout=20)
js_con=web_data.json()
#获取连接下一页评论的max_id
max_id=js_con['data']['max_id']
max=js_con['data']['max']
comments_list=js_con['data']['data']
forcommment_itemincomments_list:
Obj={
'commentor_id':commment_item['user']['id'],
'commentor_name':commment_item['user']['screen_name'],
'commentor_blog_url':commment_item['user']['profile_url'],
'comment_id':commment_item['id'],
'comment_text':commment_item['text'],
'create_time':formatTime(commment_item['created_at'],'%a%b%d%H:%M:%S+0800%Y','%Y-%m-%d%H:%M:%S'),
'like_count':commment_item['like_count'],
'reply_number':commment_item['total_number'],
'full_path':base_url+str(weibo_id),
'max_id':max_id,
'max':max
}
commentLists.append(Obj)
print("已获取第1页的评论")
returncommentLists
exceptExceptionase:
print("遇到异常")
return[]
#运用递归思想，爬取剩余页面的评论。因为后面每一页的url都有一个max_id，这只有从前一个页面返回的数据中获取。
deforther_page_comments(count,weibo_id,url,headers,max,max_id):
ifcount<=max:
try:
ifcount<15:
urlNew=url+str(weibo_id)+'&mid='+str(weibo_id)+'&max_id_type=0'
else:
urlNew=url+str(weibo_id)+'&mid='+str(weibo_id)+'&max_id='+str(max_id)+'&max_id_type=1'
web_data=requests.get(url=urlNew,headers=headers,cookies=Cookie,timeout=10)
#成功获取数据了，才执行下一步操作
ifweb_data.status_code==200:
js_con=web_data.json()
#print('js_con：',js_con)
#评论开启了精选模式，返回的数据为空
ifjs_con['ok']!=-100:
	#获取连接下一页评论的max_id
max_id=js_con['data']['max_id']
max=js_con['data']['max']
comments_list=js_con['data']['data']
#print('comments_list:',comments_list)
forcommment_itemincomments_list:
Obj={
'commentor_id':commment_item['user']['id'],
'commentor_name':commment_item['user']['screen_name'],
'commentor_blog_url':commment_item['user']['profile_url'],
'comment_id':commment_item['id'],
'comment_text':commment_item['text'],
'create_time':formatTime(commment_item['created_at'],'%a%b%d%H:%M:%S+0800%Y','%Y-%m-%d%H:%M:%S'),
'like_count':commment_item['like_count'],
'reply_number':commment_item['total_number'],
'full_path':base_url+str(weibo_id),
'max_id':max_id,
'max':max
}
commentLists.append(Obj)
count+=1
print("已获取第"+str(count+1)+"页的评论。")
orther_page_comments(count,weibo_id,url,headers,max,max_id)#递归
returncommentLists
else:
return[]
exceptExceptionase:
ifcount==1:
print("遇到异常,爬虫失败")#假设连第一条数据都没有爬到，我就认为是爬虫失败
else:
return
#将数据保存到excel中
defexport_excel(exportArr,id,sheetName,excel_name):
file_path=pd.ExcelWriter(excel_name)#指定生成的Excel表格名称
#将数据保存到sheet中
pf=pd.DataFrame(exportArr)#将字典列表转换为DataFrame
order=['comment_id','commentor_name','commentor_id','commentor_blog_url','comment_text','create_time','like_count','reply_number','full_path']#指定字段顺序
pf=pf[order]
pf.reindex()
	#将列名替换为中文
columns_map={
'comment_id':'comment_id',
'commentor_name':'评论者名字',
'commentor_id':'评论者id',
'commentor_blog_url':'评论者的微博主页',
'comment_text':'评论内容',
'create_time':'发布时间',
'like_count':'点赞数',
'reply_number':'回复数',
'full_path':'微博url',
}
pf.rename(columns=columns_map,inplace=True)
pf.fillna('',inplace=True)#替换空单元格
pf.to_excel(excel_name,index=False,sheet_name=sheetName)#输出
file_path.save()#保存到表格
print('----------第',id,'篇微博的评论已经保存了---------------')
return'true'

#将数据保存到txt文件中
defexport_txt(list,txtId):
arr=[str(txtId),'',list['full_path'],'',list['commentor_name']]
commentorNameMaxLen=20#假设最大的长度为20，不足20的以空格代替，确保长度一致，避免参差不齐
lenGap=commentorNameMaxLen-len(list['commentor_name'])
foriinrange(lenGap):
arr.append('-')
arr.append(list['comment_text'])
arr.append('\n')#每一行结束要换行
file_handle.writelines(arr)

if__name__=="__main__":
output=[]
commentLists=[]#初始化存储一个微博评论数组
weibo_comment=weiboComment
txt_id=1#用于记录txt数据的id
file_handle=open(txt_name,mode='w',encoding='utf-8')#打开txt文件
file_handle.writelines(['id','微博链接','评论者','','评论内容\n'])#写入头部的字段名字

##存储每一篇微博的评论数据
forind,iteminenumerate(weibo_comment):
output=first_page_comment(item['weibo_id'],url,headers)
iflen(output)>0:
maxPage=output[-1]['max']
maxId=output[-1]['max_id']
#如果结果不只一页，就继续爬
if(maxPage!=0):
ans=orther_page_comments(0,item['weibo_id'],url,headers,maxPage,maxId)
#如果评论开启了精选模式，最后一页返回的数据是为空的
ifans!=[]:
bool=export_excel(ans,item['id'],item['sheet_name'],item["excel_name"])
else:
bool=export_excel(commentLists,item['id'],item['sheet_name'],item["excel_name"])
ifbool=='true':
commentLists=[]#将存储的数据置0
forlistinans:
txt_id=txt_id+1#用于记录txt数据的id
export_txt(list,txt_id)
else:
print('----------------该微博的评论只有1页-----------------')
file_handle.close()#保存到txt
data_process.data_process()#调用数据处理及图形显示函数
~~~

### data_process.py

实现数据处理以及图形化显示及保存函数。

~~~python
import jieba as jb
import pandas as pd
from config import weiboComment
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

jb.setLogLevel(jb.logging.INFO)
def data_process():
    def comment_get(comments):
        content = re.sub(r"</?(.+?)>", "", comments) # 去除标签
        comment = re.sub(r"\s+", "", content)  # 去除空白字符
        return comment

    # 读取文件excel
    file_list = []
    for weibocomment in weiboComment:
        file_list.append(weibocomment["excel_name"])
    pf = pd.DataFrame()
    # 获取微博的评论信息
    for file_path in file_list:
        pf = pf.append(pd.read_excel(io=file_path),ignore_index=True)
    # 获取所有评论内容
    comment_df = pd.DataFrame(pf["评论内容"])
    # 处理所有评论将附带的html标签样式删除
    comment_df = comment_df["评论内容"].map(comment_get)

    comment_ls = comment_df.to_list()
    txt = ""
    for comment_st in comment_ls:
        txt += comment_st
    txt = jb.lcut(txt)
    d = {}
    for i in txt:
        if len(i) == 1:
            continue
        else:
            d[i] = d.get(i, 0) + 1
    ls1 = list(d.items())
    ls1.sort(key=lambda x: x[1], reverse=True)
    tokenstrs = ""
    for date in ls1:
        tokenstrs += date[0] + " "
    with open("./comments/onlycomments.txt","w") as fp:
        fp.write(tokenstrs)
    image = Image.open('./image/ditu.png')
    graph = np.array(image)
    mywcl = WordCloud(
        max_font_size=30,
        min_font_size=10,
        random_state=50,
        background_color='white',
        width=900, height=600,
        font_path='C:/Windows/Fonts/msyh.ttc',
        mask=graph
    ).generate(tokenstrs)
    plt.imshow(mywcl)
    plt.axis('off')
    plt.show()
    mywcl.to_file('./image/分词.png')

    dls = []
    nls = []
    for data in ls1:
        dls.append(data[0])
        nls.append(data[1])
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.bar(range(len(dls[0:15])),nls[0:15],tick_label=dls[0:15])
    plt.xlabel("词汇")
    plt.ylabel("出现次数")

    plt.savefig('./image/柱状图.png')
    plt.show()

    plt.close()
~~~



