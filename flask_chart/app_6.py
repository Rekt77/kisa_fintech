from flask import Flask,Blueprint,jsonify,request
import json

app = Flask(__name__)

@app.route("/json")
def to_json():
    #{"name":"taeil"}
    #{"이름":"이태일"}
    return json.dumps({"이름":"이태일"},ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)