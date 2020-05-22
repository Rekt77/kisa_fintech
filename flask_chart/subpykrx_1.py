from pykrx import stock
import pandas as pd
import numpy as np

class krxModule:
    #key==index
    #value==dictionary{colums:value}
    #이걸 통해서 티커이름:{종목명,시가,종가,변동폭,등락률,거래량,거래대금}을 만들거임
    def to_dict(self,df):
        return {df.iloc[i].name:df.iloc[i].to_dict() for i in range(len(df))}

    def getTop10(self,start,end):
        # df인 이유는 데이터프레임 객체이기 때문
        # 모든 종목에 대한 데이터 프레임이 반환됨
        df = stock.get_market_price_change_by_ticker(start,end)

        #sort_values는 데이터프레임 객체에 존재하는 함수 등락률을 기준으로 내림차순 정렬 할것임
        #head함수를 통해 데이터 슬라이싱
        return self.to_dict(df.sort_values("등락률",ascending=False).head(10))
#test
df = stock.get_market_price_change_by_ticker("20200501","20200503")
#print(df.iloc[0].to_dict())
print(df.iloc[0])# --> 티커
# df에 어떤 요소가 있는지 확인
# 우리는 기간별 등락률 top10을 구할거기 때문에 등락률 컬럼을 기준으로 데이터를 만들거임
# df.iloc[i].to_dict() --> {종목명:?,시가:?,종가:?,변동폭:?,등락률:?,거래량:?,거래대금:?}