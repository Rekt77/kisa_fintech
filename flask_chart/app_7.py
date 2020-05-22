from flask import Flask,request,jsonify
from CustomJSONencoder import CustomJSONEncoder
from subpykrx import krxModule

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# krxModule을 불러오기
myKrx = krxModule()

@app.route("/top10",methods=["GET","POST"])
def top10():
    if request.method == "GET":
        return """
        <form action='/top10' method='post'>
        <input name='start' type='date'>
        <input name='end' type='date'>
        <input type='submit'>
        </form>
        """
    else:
        start = request.form.to_dict(flat=True)['start'].replace("-","")
        end = request.form.to_dict(flat=True)['end'].replace("-","")
        #myKrx에서 getTop10
        df = myKrx.getTop10(start,end)
        
        # 정상작동?
        # 딕셔너리가 순서대로 나오지 않은 이유 설명
        # 이 딕셔너리는 추후에 chart.js에 들어갈 데이터이기 때문에 정렬상태가 상관없다고 설명
        return jsonify(df)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)