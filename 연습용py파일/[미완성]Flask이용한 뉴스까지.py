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



app = Flask(__name__)


@app.route('/')
def index():
    f = open('text1.csv', 'r')
    stock_list = csv.reader(f)
    stock_list2 = ['000020.KS','000040.KS','000060.kS']
    stock_list3 = ['000020','000040','000060']
    fig = make_subplots(rows=5, cols=2)
    for i, list in enumerate(stock_list2):
        data = yf.download(list, start = '2019-01-01')
        df = data['Adj Close']
        url = "https://finance.naver.com/item/news_news.nhn?code=000020&page=&sm=title_entity_id.basic&clusterId="
        dfnews = pd.read_html(url, header = 0 , encoding='euc-kr')
        dfnews[0]
        
        fig = fig.add_trace(go.Scatter(x=df.index, y=df), row=1+i, col=1)
        fig = fig.add_trace(go.Scatter(x=[1.5],y=[0.75],
        text=[dfnews[0]], mode="text"), row=1+i, col=2)

    return fig.show()

@app.route('/news/')
def news():
    f = open('text1.csv', 'r')
    stock_list = csv.reader(f)
    stock_list2 = ['000020.KS','000040.KS','000060.kS']
    stock_list3 = ['000020','000040','000060']
    for i in stock_list3:
        url = "https://finance.naver.com/item/news_news.nhn?code={}&page=&sm=title_entity_id.basic&clusterId=".format(i)
        dfnews = pd.read_html(url, header = 0 , encoding='euc-kr')
        dfnews[0]
        

    return print(dfnews[1])

if __name__ == "__main__":
    app.run(debug=True)





# df = web.DataReader(
#     'yahoo',
#     dt(2017, 1, 1), 
#     dt.now()
# )  