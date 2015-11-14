from flask import Flask
from werkzeug import serving
from werkzeug._internal import _log


class LimitLogHandler(serving.WSGIRequestHandler):
    def log(self, type, message, *args):
        msg = message % args
        _log(type, '%s [%s]\n' % (msg, self.client_address[0]))


app = Flask(__name__)

index = open("index.html").read()


@app.route("/")
def hello():
    return index


if __name__ == "__main__":
    import logging

    # logging.basicConfig(filename='msm-site.log', level=logging.DEBUG,
    #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename='/var/log/msm-site.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app.run(request_handler=LimitLogHandler)
