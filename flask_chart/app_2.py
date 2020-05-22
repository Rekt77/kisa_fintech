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
        #replace 함수 추가해서 pykrx에 넣을 수 있게 만들기
        start = request.form.to_dict(flat=True)['start'].replace("-","")
        end = request.form.to_dict(flat=True)['end'].replace("-","")
        return "%s, %s"%(start,end)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)