from flask import Flask, render_template, url_for
from pandas.io.html import read_html
import plotly.express as px
import pandas as pd
from pandas_datareader import data as web 
from datetime import datetime as dt
import csv
from os import write
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html
import yfinance as yf
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import codecs
from flaskext.markdown import Markdown
import plotly

app = Flask(__name__,static_folder='./static/')
app.jinja_env.filters['zip'] = zip
Markdown(app)

@app.route('/')
def index():
    listnews = []
    listgraph = []
    money_tables = []
    f = open('./static/stockcode/stockcode.csv', 'r')
    stock_list = csv.reader(f)
    for lists in stock_list:
        for i in lists:
            # url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(i)     
            # url = '{url}&page={page}'.format(url=url, page=1)
            # print(url)
            # header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'}  
            # res = requests.get(url, headers = header)
            # df = pd.read_html(res.text, header=0, encoding='euc-kr')[0]
            
            # for page in range(2,31):
            #     url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(i)     
            #     url = '{url}&page={page}'.format(url=url, page=page)
            #     # print(url)
            #     header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'}  
            #     res = requests.get(url, headers = header)
            #     A = pd.read_html(res.text, header=0, encoding='euc-kr')[0]
            #     df = df.append(A, ignore_index=True)
            #     # print(df)

            # # df.dropna()를 이용해 결측값 있는 행 제거 
            # df = df.dropna() 

            # # 한글로 된 컬럼명을 영어로 바꿔줌 
            # df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 
            # # 데이터의 타입을 int형으로 바꿔줌 
            # df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 

            # # 컬럼명 'date'의 타입을 date로 바꿔줌 
            # df['date'] = pd.to_datetime(df['date']) 

            # # 일자(date)를 기준으로 오름차순 정렬 
            # df = df.sort_values(by=['date'], ascending=True) 

            # # # 단순형 그래프 그리기
            # # plt.figure(figsize=(10,4))
            # # plt.plot(df['date'], df['close'])
            # # plt.xlabel('date')
            # # plt.ylabel('close')
            # # plt.tick_params(
            # #     axis='x',          # changes apply to the x-axis
            # #     which='both',      # both major and minor ticks are affected
            # #     bottom=False,      # ticks along the bottom edge are off
            # #     top=False,         # ticks along the top edge are off
            # #     labelbottom=True) # labels along the bottom edge are off
            # # plt.savefig('./static/image/stocklist/'+ i + ".png")
            # # plt.show()
        

            # # 반응형 그래프 그리기
            # fig = px.line(df, x='date', y='close', title='{}의 종가(close) Time Series'.format(i))

            # fig.update_xaxes(
            #     rangeslider_visible=True,
            #     rangeselector=dict(
            #         buttons=list([
            #             dict(count=1, label="1m", step="month", stepmode="backward"),
            #             dict(count=6, label="6m", step="month", stepmode="backward"),
            #             dict(count=1, label="YTD", step="year", stepmode="todate"),
            #             dict(count=1, label="1y", step="year", stepmode="backward"),
            #             dict(step="all")
            #         ])
            #     )
            # )
            # fig.write_html('./static/image/stocklist1/'+ i + ".html")
            
        # #### html로 저장된 graph html 파일 그대로 불러오기 ####
        #     graphfile = "./static/image/stocklist1/{}.html".format(i)
        #     gp = open(graphfile, "r", encoding='utf-8') 
        #     G= gp.read()
        #     listgraph.append(G)
        

        ### 여기서부터 뉴스 ###
            # url = "https://finance.naver.com/item/news_news.nhn?code={}&page=&sm=title_entity_id.basic&clusterId=".format(i)
            # # url = "https://finance.naver.com/item/news_news.nhn?code=000020&page=&sm=title_entity_id.basic&clusterId="
            # dfnews = pd.read_html(url, header = 0 , encoding='euc-kr')
            # Z =dfnews[0].to_html
            # listnews.append(Z)
            # end_news = dfnews[0].to_html()


            # #### 뉴스를 html로 저장하기 ####
            # url = "https://finance.naver.com/item/news_news.nhn?code={}&page=&sm=title_entity_id.basic&clusterId=".format(i)
            # dfnews = pd.read_html(url, header = 0 , encoding='euc-kr')
            # # Z =dfnews[0].to_html
            # # listnews.append(Z)
            # dfnews[0].to_html("./static/news/"+i+'.html')

            # #### 뉴스를 html을 마크다운으로 저장하기 ####
            # url = "https://finance.naver.com/item/news_news.nhn?code={}&page=&sm=title_entity_id.basic&clusterId=".format(i)
            # dfnews = pd.read_html(url, header = 0 , encoding='euc-kr')
            # # Z =dfnews[0].to_html
            # # listnews.append(Z)
            # dfnews[0].to_markdown("./static/news/"+i+'.markdown')



            # #### html로 저장된 뉴스 csv파일 그대로 불러오기 ####
            # csvfile = "./static/news/{}.csv".format(i)
            # fp = open(csvfile, "r", encoding='utf-8') 
            # Z= fp.read()
            # listnews.append(Z)


            # #### html로 저장된 뉴스 판다스 통해 표로 읽기 ####
            # csvfile = "./static/news/{}.html".format(i)
            # dfnews = pd.read_html(csvfile, header = 0 , encoding='utf-8')
            # Z =dfnews[0]
            # listnews.append(Z)

            # #### html로 저장된 뉴스 csv로 만들고 판다스 통해 표로 읽기 ####
            # csvfile = "./static/news/{}.csv".format(i)
            # dfnews = pd.read_csv(csvfile, header = 0 , encoding='utf-8')
            # Z =dfnews
            # listnews.append(Z)

            #### html로 저장된 뉴스 html 파일 그대로 불러오기 ####
            csvfile = "./static/news/{}.html".format(i)
            fp = open(csvfile, "r", encoding='utf-8') 
            Z= fp.read()
            listnews.append(Z)

            # #### html로 저장된 뉴스 마크다운 불러오기 ####
            # csvfile = "./static/news/{}.markdown".format(i)
            # fp = open(csvfile,"r", encoding='utf-8') 
            # Z= fp.read()
            # listnews.append(Z)
            
            # dfnews1=codecs.open(csvfile, 'r', encoding='utf-8')
            # J = dfnews1.read()
            # K = dfnews1.readlines()
            # dfnews = read_html(csvfile, header = 0 , encoding='utf-8')
            # Z =dfnews[0].to_html
            # listnews.append(Z)
            #잠시만안녕



        #### 여기서부터 재무재표 ####
            # #### html 파일로 만들기 ####
            # url = "https://finance.naver.com/item/main.nhn?code={}".format(i)
            # df = pd.read_html(url, header = 0 , encoding='euc-kr')
            # df[3].to_html("./static/money_tables/"+i+'.html')


            #### html로 저장된 재무재표 html 파일 그대로 불러오기 ####
            moneyfile = "./static/money_tables/{}.html".format(i)
            mt = open(moneyfile, "r", encoding='utf-8') 
            M= mt.read()
            money_tables.append(M)


    return render_template('index.html', listnews = listnews , lists = lists , money_tables = money_tables )



# app.config['IMG_FOLDER'] = os.path.join('static','image') # 이미지 파일의 경로지정
# path = "./static/image/stocklist/"

# @app.route('/stocklist/')
# def gallery():

#     # full_filepath = os.listdir(path)
#     return render_template("stocklist.html", pics ="./static/image/stocklist/")
#     # return render_template("stocklist.html")

@app.route('/SomeFunction')
def SomeFunction():
    print('In SomeFunction')
    return "Nothing"


if __name__ == "__main__":
    app.run(debug=True)

