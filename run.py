from flask import Flask

app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return open("index.html").read()


if __name__ == "__main__":
    app.run()
