# practice flask๐งโ๐

## flask ๊ตฌ๋ ๋ฐฉ๋ฒ

### virtualenv

์งํํ๊ณ  ์๋ ๋ ๋ง์ ํ๋ก์ ํธ๋ค์ด ์๋ก ๋ค๋ฅธ Python ๋ฒ์ ์์ ์๋ํด์ผ ํ๋ค๊ฑฐ๋ ํน์ ์๋ก ๋ค๋ฅธ ๋ฒ์ ์ Python ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ค ์์ ์๋ํด์ผ ํ๋ค๋ฉด virtualenv๋ฅผ ์ด์ฉํ์ฌ Python์ ์๋ฌด๋ฐ ๋ฌธ์  ์์ด ๊ฐ๊ฐ์ ํ๋ก์ ํธ ํ๊ฒฝ์ ๋ง๊ฒ ๋ค์ค์ค์น๊ฐ ๊ฐ๋ฅํ๋๋ก ํด์ค๋ค.

### mac OS ํน์ Linux์ผ ๊ฒฝ์ฐ

```sh
sudo easy_install virtualenv
```

ํน์

```sh
sudo pip install virtualenv
```

๋ก ์ค์น ๊ฐ๋ฅํ๋ค.

### ์์ ๋ง์ ์คํํ๊ฒฝ ๋ง๋ค๊ธฐ

```sh
mkdir myproject
cd myproject
virtualenv venv
```

### ์คํํ๊ฒฝ ํ์ฑํ

```sh
. venv/bin/activate
```

### Flask ์ค์น

```sh
sudo pip install Flask
```
