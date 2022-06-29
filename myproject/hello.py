import os
from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['new_file']
  f.save(f.filename)
  return redirect('/hello')

if __name__ == '__main__':
    app.run()
