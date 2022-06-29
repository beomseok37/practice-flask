# Flask 기본

기본 Flask 어플리케이션의 모습

**hello.py**

```Python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

파일의 이름을 flask.py로 지을 경우 Flask자체와 충돌이 날 수 있다.
