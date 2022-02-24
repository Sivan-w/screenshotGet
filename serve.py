from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if 'myImg' in request.files:
            idName = request.form.get('id')
            objFile = request.files.get('myImg')
            objFile.filename = idName + '.jpg'
            # print(11)
            strFilePath = "C:/Users/19759/Desktop/272screenshot/" + objFile.filename
            # print(22)
            objFile.save(strFilePath)
            return render_template('success.html')
        else:
            return "error"
    else:
        return "error"


if __name__ == '__main__':
    app.run(
        host='192.168.2.189',
        port=8089
    )
