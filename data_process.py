#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：weibocomments 
@File    ：data_process.py
@IDE     ：PyCharm 
@Author  ：
@Date    ：2022/6/12 0012 下午 11:18 
'''


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