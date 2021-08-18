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


url = "./static/news/000020.html"
# dfnews = pd.read_html(url, header = 0 , encoding='utf-8')
fp = open(url,"r", encoding='utf-8') 
Z= fp.read()
print(Z)




# # Z =dfnews[0].to_html
# Z =dfnews[0]['제목']
# print(Z)
