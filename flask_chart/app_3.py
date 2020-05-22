from flask import Flask,request,jsonify
from subpykrx import krxModule

app = Flask(__name__)

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

        # 출력은 잘되었음
        print(df)
        
        # df는 딕셔너리 형태로 변해있기때문 될거라고 생각
        return jsonify(df)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)