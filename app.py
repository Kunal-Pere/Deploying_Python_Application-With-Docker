from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a simple web application from kpz software pvt. ltd.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
