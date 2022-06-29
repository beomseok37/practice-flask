# Flask 기본

## 기본 Flask 어플리케이션의 모습

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

### 실행 방법

```sh
python hello.py
```

'http://127.0.0.1:5000/' 로 접속 시 라우팅된 페이지로 이동할 수 있다.

### 세부 코드 파악

`app - Flask(__name__)`
Flask class의 인스턴스를 생성. 인자로 모듈이나 패키지의 이름을 넣는다.

```py
def hello_world():
    return 'Hello World!'
```

`route()`데코레이터를 사용해서 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려준다. 사용자 브라우저에 보여줄 메시지를 리턴한다.

```py
if __name__ == '__main__':
    app.run()
```

어플리케이션 실행. 소스파일을 python 인터프리터를 이용해서 직접 실행한다면 `if __name__ == '__main__':` 이 문장은 우리가 실행한 서버가 현재 동작되는 유일한 서버라는 것을 보장한다.

서버 중지 시 control-C

## 디버그 모드

```py
app.debug = True
app.run()
#혹은
app.run(debug=True)
```

`run()`메소드는 로컬 개발 서버를 실행시키기에는 좋지만 코드 변경후에 수동으로 재시작해야한다.<br>
플라스크는 그런 번거러운 것을 개선한 방식을 제공한다. 디버그모드를 지원할 경우, 서버는 코드 변경을 감지하고 자동으로 리로드하고, 문제가 발생하면 문제를 찾을 수 있도록 디버거를 제공한다.
