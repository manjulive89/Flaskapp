# blog.py
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/blog')
def blog():
    return "My Blog"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)
