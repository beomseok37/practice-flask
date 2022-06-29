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

## 라우팅

기본 예시

```py
@app.route(‘/’)
def index():
  return ‘Index Page’

@app.route(‘/hello’)
def hello():
  return ‘Hello World’
```

`route()` 데코레이터는 함수와 URL을 연결해준다.

### 변수 규칙

<variable_name>으로 URL에 특별한 영역으로 표시해야한다. 그 부분은 함수의 키워드 인수로써 넘어간다.<br>
<converter:variable_name>으로 규칙을 표시하여 변환기를 추가할 수 있다.

```py
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

다음과 같은 변환기를 제공한다.
|||
|-|-|
|int|accepts integers|
|float|like int but for floating point values|
|path|like the default but also accepts slashes|
|||

### 유일한 URL과 리디렉션 동작

```py
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

URL정의에 있어서 뒷 슬래쉬가 있을 경우, 파일시스템의 폴더와 유사하게 뒷 슬래쉬 없이 URL접근하면, Flask가 뒷 슬래쉬를 가진 정규 URL로 고쳐준다.<br>
URL정의에 있어서 뒷 슬래쉬가 없을 경우, 뒷 슬래쉬를 포함해서 URL에 접근하면 "404 Page not Found" 에러를 유발한다.<br>
