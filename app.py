from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/test2')
def hello2():
    return "222222222"

if __name__ == '__main__':
    app.run(debug=True)
