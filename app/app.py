from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"

@app.route("/test", methods=["post"])
def test():
        print("天気")
        return "It Works!"
