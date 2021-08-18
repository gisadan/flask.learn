from os import write
import csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import clipboard
from pyperclip import ENCODING

#잠시만안녕
f = open('text1.csv', 'r')
stock_list = csv.reader(f)
for txt in stock_list:

    for i in txt:
        # 페이지 이동
        url = "https://finance.naver.com/item/news_news.nhn?code={}&page=&sm=title_entity_id.basic&clusterId=".format(i)

        # html 파일 읽어오기
        df = pd.read_html(url, header = 0 , encoding='euc-kr')
        print(df[0])
        # stock_data_raw = df[3]

        # # 첫 행을 columns로 만들어.
        # stock_data_raw_1 = stock_data_raw.rename(columns=stock_data_raw.iloc[0])

        # # 2번 째 행을 삭제해(첫 행이랑 똑같으니까)
        # stock_data_raw_2 = stock_data_raw_1.drop(stock_data_raw_1.index[1])

        # # stock_data_raw_2 가 행열 전환전에 딱 쓸만한 것!

        # # stock_data_raw_2 가 행열 전환에 맞게 행 하나 더 지워!
        # stock_data_raw_3 = stock_data_raw_2.drop(stock_data_raw_1.index[0])

        # # 행/열 전환
        # stock_data_raw_4 = stock_data_raw_3.transpose()	#행 열 전환
        # stock_data_raw_4.rename(columns=stock_data_raw_4.iloc[0], inplace=True)	# 행열이 전환된 데이터프레임의 열 이름 제대로 수정
        # stock_data_raw_5 = stock_data_raw_4.drop(stock_data_raw_4.index[0])
        # stock_data_raw_5 = stock_data_raw_5.replace('-','NaN')
        # stock_data_raw_6 = stock_data_raw_5.astype(float)

        # if stock_data_raw_6['당기순이익'].lt(0).any() or stock_data_raw_6['부채비율'].gt(100).any() or stock_data_raw_6['당좌비율'].lt(100).any():  # (1)
        #     continue
        # else:
        #     print(i + '확인')             

        