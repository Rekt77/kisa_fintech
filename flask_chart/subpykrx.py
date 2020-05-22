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

    # chartJSON을 만들거임
    # 딕셔너리 인풋은 getTop10리턴값
    def chartJSON(self,dic):
        #딕셔너리를 이터레이팅
        #키값은 버릴거기 때문에 _ 처리
        #종목명과 등락률만 추출
        tmp_dic = {ticker["종목명"]:ticker["등락률"] for _,ticker in dic.items()}

        #labels는 tmp_dic의 키값
        labels = list(tmp_dic.keys())
        #labels는 tmp_dic의 밸류값
        datas = list(tmp_dic.values())

        #rgb값을 만들어줌 0~255 랜덤
        #labels길이랑 rand길이를 맞춰줌
        rand = [[np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)] for _ in range(len(labels))]

        #bg생상과 테두리 색상 만들어줌
        backgroundColors = ['rgba(%d,%d,%d,0.2)'%(rand[i][0],rand[i][1],rand[i][2]) for i in range(len(labels))]
        borderColors = ['rgba(%d,%d,%d,1)'%(rand[i][0],rand[i][1],rand[i][2]) for i in range(len(labels))]

        #chart.js홈페이지에서 json분석
        json_ = {
            # 타입은 bar
            'type': 'bar',
            # 데이터
            'data': {
                # 라벨링
                'labels': labels,
                'datasets': [{
                    # 라벨이름
                    'label': '등락률',
                    # datas는 라벨에 대응되는 데이터
                    'data': datas,
                    # 그래프는 랜덤색상
                    'backgroundColor': backgroundColors,
                    # 테두리는 랜덤색상
                    'borderColor': borderColors,
                    'borderWidth': '1'
                }]
            },
            'options': {
                'responsive': False,
                'scales': {
                    'yAxes': [{
                        'ticks': {
                            'beginAtZero': True
                        }
                    }]
                },
            }
        }
        return json_