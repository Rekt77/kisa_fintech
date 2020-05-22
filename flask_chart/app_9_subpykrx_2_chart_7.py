from flask import Flask,request,jsonify
from CustomJSONencoder import CustomJSONEncoder
from subpykrx import krxModule
from flask_cors import CORS,cross_origin

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# cors 해결
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# krxModule을 불러오기
myKrx = krxModule()

# GET은 더 이상 필요없음
@app.route("/top10",methods=["POST"])
def top10():
    #json형태의 데이터를 받을 것임.
    if request.json:
        #출력
        print(request.json)
        df = myKrx.getTop10(request.json['start'],request.json['end'])

        # 차트 데이터 넘겨주기
        return jsonify(myKrx.chartJSON(df))
    else:
        return jsonify({'msg':'no input vlaue'})

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)