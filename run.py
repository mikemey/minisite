from flask import Flask

app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return index


if __name__ == "__main__":
    import logging

    logging.basicConfig(filename='/var/log/msm-site.log', level=logging.DEBUG)

    app.run()
