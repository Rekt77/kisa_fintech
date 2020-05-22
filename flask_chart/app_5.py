from flask import Flask,jsonify,request
from CustomJSONencoder import CustomJSONEncoder
import numpy as np
app = Flask(__name__)

#customJSONEncoder 만든 것 apply
app.json_encoder = CustomJSONEncoder

@app.route("/json")
def to_json():
    # 테스트: 정상작동
    return jsonify({"abc":np.int64(123)})

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)