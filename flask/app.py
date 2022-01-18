# flask_web/app.py

from flask import Flask
from flask import abort
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container in a pipeline!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')