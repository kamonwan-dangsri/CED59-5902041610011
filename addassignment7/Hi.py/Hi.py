from flask import  Flask, escape, request

app = Flask(_name_)

@app.route('/')
def index():
    return "Hello World"
if __name__ = '__main__':
    app.run()
