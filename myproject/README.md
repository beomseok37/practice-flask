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

## HTTP 메소드

기본적으로 GET방식으로 제공되지만, `route()`데코레이터에 methods 인자를 제공하면 다른 방식으로 변경할 수 있다.

```ps
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

## 템플릿 렌더링

```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

`render_template()`메소드를 사용하여 템플릿을 렌더링해줄 수 있고, 인자를 넘겨줄 수도 있다.<br>
Flasksms templates폴더에서 템플릿을 찾으므로 해당 폴더 내에 템플릿들을 넣어주어야 한다.

### 템플릿예제

```html
<!DOCTYPE html>
<title>Hello from Flask</title>
{% if name %}
<h1>Hello {{ name }}!</h1>
{% else %}
<h1>Hello World!</h1>
{% endif %}
```

템플릿에서 상속이 유용하게 쓰인다. 자동 이스케이핑은 켜져있고, name이란 변수가 인자로 전해졌다면 자동으로 이스케이핑 된다.

## 요청 데이터 접근

클라이언트가 서버로 보내는 데이터는 `request`객체에 의해 제공된다.

### 컨텍스트 로컬

웹에서 요청이 들어오면, 웹 서버는 새로운 쓰레드를 생성한다. Flask는 내부적으로 요청을 처리할 때, 현재 처리되는 쓰레드를 활성화된 문맥이라고 간주하고 실행되는 어플리케이션과 WSGI환경을 그 문맥에 연결한다.<br>
유닛테스트를 할 경우 요청 걕체에 의한 코드는 깨지게 되는데 그 이유는 요청이 들어오지 않아 활성화된 문맥이 없으므로 요청 객체가 존재하지 않기 때문이다. 그래서 문맥관리자 `test_request_context()`를 사용한다.<br>
Flaskdptj 이런 객체들은 보통 객체가 아닌 전역 객체들이다. 이 객체들은 실제로 **어떤 특정한 문맥**에서 생성되는 객체들에 대한 대리자들이다.

### 요청 객체 (기본)

```py
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 아래의 코드는 요청이 GET 이거나, 인증정보가 잘못됐을때 실행된다.
    return render_template('login.html', error=error)
```

- method속성을 이용하여 http 메소드를 확인할 수 있다.
- form속성을 이용하여 전달된 데이터에 접근할 수 있다.
- GET 메소드와 같이 URL로 넘겨진 파라미터에 접근하려면 `args`속성을 사용한다.
  > ```
  > key = request.args.get('key','')
  > ```
  >
  > `args`속성을 사용할 경우 get을 사용하거나 KeyError예외를 처리하여 URL접근할 것을 추천한다. 왜냐하면 사용자가 임의로 URL을 변경할 수도 있기 때문이다.

### 파일 업로드

HTML form에 `enctype="multipart/form-data"`를 설정<br>

```py
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

`request`객체의 속성인 `files`를 사용한다. `files`는 file명을 key로 해당 파일을 value로 하는 dictionary이다.<br>
`files`속성으로 얻어온 file에 대한 참조는 표준 파이썬 file객체처럼 행동한다. 그래서 `save()`메소드를 가지고 있어 서버의 파일시스템에 저장할 수 있다.

### 쿠키

쿠키에 접근하기 위해서는 `request` 객체의 `cookies`속성을 사용한다.<br>
쿠키를 저장하기 위해서는 `response` 객체의 `set_cookie`메소드를 사용한다.<br>
Reading cookies

```py
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
```

Storing cookies

```py
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```
