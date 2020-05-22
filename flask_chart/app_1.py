from flask import Flask,request
from subpykrx import krxModule

app = Flask(__name__)

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
        #이거 실행하고 pykrx에 값을 넣을 때 날짜 데이터가 -없는 형태임을 시사
        start = request.form.to_dict(flat=True)['start']
        end = request.form.to_dict(flat=True)['end']
        return "%s, %s"%(start,end)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)