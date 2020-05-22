from flask import Flask,jsonify,request
import json
import numpy as np
app = Flask(__name__)

@app.route("/json")
def to_json():
    #{"name":"taeil"}
    #{"이름":"이태일"}
    #{"abc":np.int64(123)}
    #json.dumps({"이름":"이태일"},ensure_ascii=False)
    #customJSONencoder를 만들어주기
    return jsonify({"abc":np.int64(123)})

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)