#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：weibocomments 
@File    ：config.py
@IDE     ：PyCharm 
@Author  ：
@Date    ：2022/6/11 0011 下午 11:02 
'''
base_url = 'https://m.weibo.cn/status/'
url = 'https://m.weibo.cn/comments/hotflow?id='

# excel_name = r'weibo_comments.xls'
txt_name = './comments/weibo_comments.txt'

ALF = 1583630252
MLOGIN = 1
M_WEIBOCN_PARAMS = 'oid%3D4469046194244186%26luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803'
SCF = 'AjheAPuZRqxmyLT-kTVnBXGduebXE6nZGT5fS8_VPbfADyWHQ_WyoRzZqAJNujugOFYP1tUivrlzK2TGTx83_Qo.'
SSOLoginState = 1581038313
SUB = '_2A25zOMq5DeRhGeNM6FUX8S_EzDqIHXVQwtbxrDV6PUJbktAKLVPhkW1NTjKs6wgXZoFv2vqllQWpcwE-e9-8LlMs'
SUBP = '0033WrSXqPxfM725Ws9jqgMF55529P9D9W58TWlXMj17lMMvjhSsjQ1p5JpX5K-hUgL.Fo-Ee0MceK2RS0q2dJLoIEXLxKqLBozL1h.LxKML1-BLBK2LxKML1-2L1hBLxK-LBKqL12BLxK-LBKqL12Bt'
SUHB = '0BLYTPzIKSGsDo'
WEIBOCN_FROM = 1110006030
XSRF_TOKEN = '5dcf70'
_T_WM = 64204543757

Cookie = {
    'Cookie':  "login_cookie"
}

headers = {
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 通过ajax请求形式获取数据
    'X-XSRF-TOKEN': 'aa8bed',
    'Accept': 'application/json, text/plain, */*'
}
# 数据id号，要爬取的微博的id号，以及导出到excel对应的sheet名
weiboComment = [{
    'id':1,
    'weibo_id': 4775326871978967,
    'sheet_name': 'file_tab1',
    'excel_name': r'./comments/weibo_comments1.xls'
},{
    'id': 2,
    'weibo_id': 4775440936339631,
    'sheet_name': 'file_tab1',
    'excel_name': r'./comments/weibo_comments2.xls'
},{
    'id': 3,
    'weibo_id': 4775131773930646,
    'sheet_name': 'file_tab1',
    'excel_name': r'./comments/weibo_comments3.xls'
},{
    'id': 4,
    'weibo_id': 4778915023822520,
    'sheet_name': 'file_tab1',
    'excel_name': r'./comments/weibo_comments4.xls'
},{
    'id': 5,
    'weibo_id': 4770173918380517,
    'sheet_name': 'file_tab1',
    'excel_name': r'./comments/weibo_comments5.xls'
}]

# 忽略警告信息
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

