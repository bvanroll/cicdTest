from flask import Flask
import requests

app = Flask(__name__)

URL = "http://server-check:6000"


@app.route('/')
def doRequest():
    return "it works"

@app.route('/check')
def itWorks():
    return requests.get(URL).json()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)