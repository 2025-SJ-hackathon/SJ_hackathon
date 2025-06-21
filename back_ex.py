# app.py
from flask import Flask, jsonify

# Flask 인스턴스 생성
app = Flask(__name__)

# 루트 URL('/')로 접근하면 이 함수가 실행됨
@app.route('/') # 바로 아래 함수만 실행
def hello():
    return 'Hello, Flask!'

@app.route('/') # / : 홈페이지 주소 | /data : API 응답 등 데이터 제공하는 별로 경로
def send_json():
    sample_data = {
        "name": "김철수",
        "age": 30,
        "skills": ["Python", "Flask", "React"]
    }
    return jsonify(sample_data)

# 예를 들자면
'''
1. 프론트에서 사진 촬영 > AI로 사진 전송
2. AI(CNN?) 에서 헤당 사진 레이블 출력
3. 메뉴 레이블을 포함하는 가게명 DB에서 뽑아내기
4. json으로 프론트에 보내기
'''


# 이 파일을 직접 실행할 때만 Flask 앱 실행
if __name__ == '__main__':
    app.run(debug=True)


'''# api.py
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
    # 포트 변경
    # app.run(debug=True, port=8080)'''

'''
<!-- 템플릿 및 상속 예시 -->
<!-- 부모 템플릿(base.html) -->
<html>
  <head>
    <title>Hi Flask</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>

<!-- 자식 템플릿(index.html) -->
{% extends "base.html"  %}
{% block content %}
  <title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
{% endblock %}
'''
