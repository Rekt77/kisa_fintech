from flask.json import JSONEncoder
import numpy as np

class CustomJSONEncoder(JSONEncoder):
    # override
    # CustomeJSONEncoder가 flask JSONEncoder를 상속하여 인코딩 방식을 변경
    # **kwargs는 flask JSONEncoder가 가지고 있는 모든 파라미터를 딕셔너리화 한다는 의미
    # kwargs중 ensure_ascii값을 false로변경
    def __init__(self, **kwargs):
        kwargs['ensure_ascii'] = False
        # super를 통해서 상속받은 클래스에 kwargs값을 flaskJSONEncoder의 생성자에 대입
        super().__init__(**kwargs)

    # 오버라이딩을 통해 flask JSONEncoder의 default함수를 변경
    def default(self, obj):
        try:
            # jsonify를 통해 serial화 될 객체가 np.integer형일 때 int로 변환
            if isinstance(obj, np.integer):
                return int(obj)
            # jsonify를 통해 serial화 될 객체가 np.float형일 때 int로 변환
            if isinstance(obj, np.float):
                return int(obj)
            # jsonify를 통해 serial화 될 객체를 전부 유니코드 문자열러 인코딩
            return str(obj).encode('utf-8')

        # 타입에러가 발생하면 패스
        except TypeError:
            pass
        # super를 통해 defualt함수를 호출
        return super().default(obj)