from flask import Flask, render_template
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


f = open('text2.csv', 'r')
stock_list = csv.reader(f)
for list in stock_list:
    for i in list:
        url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(i)     
        url = '{url}&page={page}'.format(url=url, page=1)
        
        print(url)
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'}  
        res = requests.get(url, headers = header)
        df = pd.read_html(res.text, header=0, encoding='euc-kr')[0]
        
        for page in range(2,21):
            url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(i)     
            url = '{url}&page={page}'.format(url=url, page=page)
            # print(url)
            header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'}  
            res = requests.get(url, headers = header)
            A = pd.read_html(res.text, header=0, encoding='euc-kr')[0]
            df = df.append(A, ignore_index=True)
            # print(df)

        # df.dropna()를 이용해 결측값 있는 행 제거 
        df = df.dropna() 

        # 한글로 된 컬럼명을 영어로 바꿔줌 
        df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 
        # 데이터의 타입을 int형으로 바꿔줌 
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 

        # 컬럼명 'date'의 타입을 date로 바꿔줌 
        df['date'] = pd.to_datetime(df['date']) 

        # 일자(date)를 기준으로 오름차순 정렬 
        df = df.sort_values(by=['date'], ascending=True) 
        plt.figure(figsize=(10,4))
        plt.plot(df['date'], df['close'])
        plt.xlabel('')
        plt.ylabel('close')
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off
        plt.savefig(company + ".png")
        # plt.show()