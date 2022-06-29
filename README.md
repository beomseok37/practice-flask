# practice flask🧑‍🎓

## flask 구동 방법

### virtualenv

진행하고 있는 더 많은 프로젝트들이 서로 다른 Python 버전에서 작동해야 한다거나 혹은 서로 다른 버전의 Python 라이브러리들 에서 작동해야 한다면 virtualenv를 이용하여 Python을 아무런 문제 없이 각각의 프로젝트 환경에 맞게 다중설치가 가능하도록 해준다.

### mac OS 혹은 Linux일 경우

```sh
sudo easy_install virtualenv
```

혹은

```sh
sudo pip install virtualenv
```

로 설치 가능하다.

### 자신만의 실행환경 만들기

```sh
mkdir myproject
cd myproject
virtualenv venv
```

### 실행환경 활성화

```sh
. venv/bin/activate
```

### Flask 설치

```sh
sudo pip install Flask
```
