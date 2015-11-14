from logging import FileHandler
from logging import INFO

from flask import Flask

app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return index


if __name__ == "__main__":
    file_handler = FileHandler('/var/log/msm-site.log')
    file_handler.setLevel(INFO)
    app.logger.addHandler(file_handler)
    app.run()
